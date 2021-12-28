import pandas;
import xlsxwriter;
import openpyxl;
lmao = 'Random1'
print("Welcome! This is the college database!")
college1 = str(input("Enter the college name:"))
print(college1)

#Reading the excel sheet 

dbx = pandas.read_excel("Colleges SAT GT 1300.xlsx", sheet_name=0)
dbr = dbx.set_index("INSTNM")
#Filter
cllg_namedb = dbr.loc[college1, :]

cllg_namedb = cllg_namedb.loc[{"UNITID", "CITY", "CONTROL", "CCBASIC", "CCUGPROF", "ADM_RATE_ALL", "SATVR75", "SATMT75", "SATMTMID", "SAT_AVG_ALL", "UGDS", "UGDS_WHITE", "UGDS_ASIAN", "TUITIONFEE_IN", "TUITIONFEE_OUT"}]

cllg_namedb.to_excel("cllg.xlsx")








