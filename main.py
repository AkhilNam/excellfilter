import pandas
from thefuzz import fuzz, process

SELECT_COLUMNS = {"UNITID", "CITY", "CONTROL", "CCBASIC", "CCUGPROF", "ADM_RATE_ALL", "SATVR75", "SATMT75", "SATMTMID", "SAT_AVG_ALL", "UGDS", "UGDS_WHITE", "UGDS_ASIAN", "TUITIONFEE_IN", "TUITIONFEE_OUT"}

print("Welcome! This is the college database.\n")

colleges = list()
while True:
    college = input("Enter college name (or n if done entering): ")
    if college == "n":
        print()
        break
    else:
        colleges.append(college)

if not colleges:
    exit("\nNo colleges entered. Quitting...")

all_names = list()
college_db = pandas.read_csv("Most-Recent-Cohorts-All-Data-Elements.csv", low_memory=False)
db_instnm = college_db.set_index("INSTNM")
columns = college_db.iloc[:, 3] # select all columns in row 0

first_college_name = colleges.pop(0)
first_college_name = process.extractOne(first_college_name, list(columns))[0] # try fuzzy match
print(f"Matched input to '{first_college_name}'")
all_names.append(first_college_name)
main_db = db_instnm.loc[first_college_name, :]
main_db = main_db.loc[SELECT_COLUMNS]

for college_name in colleges:
    college_name = process.extractOne(college_name, list(columns))[0]
    print(f"Matched input to '{college_name}'")
    all_names.append(college_name)
    college_info = db_instnm.loc[college_name, :].loc[SELECT_COLUMNS]
    main_db = pandas.merge(main_db, college_info, left_index=True, right_index=True)

print()
all_names = ", ".join(all_names)
main_db.to_excel("colleges.xlsx")
print("===================================")
print(f"Generated Excel sheet (colleges.xlsx) from {all_names}")
print("===================================")
