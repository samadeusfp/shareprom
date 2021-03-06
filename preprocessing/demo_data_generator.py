# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:16:40 2019

@author: Elkoumy
"""
import os


data_dir=os.path.join(  os.path.dirname(os.path.dirname(__file__)) ,'data')

#reading party A Data

insertion_A=""


idx=0
for line in open(data_dir+"//party_A_Loan_Process_MPC.csv"):
    line=line.strip('\n').split(',')
    if idx==0:
        idx+=1
        continue
    
    if len(line)>1:
        line.pop(2)
        str = 'row={'+",".join(line) +'};\n'
        str+='tdbInsertRow(ds, tbl, row);\n'
        insertion_A+=str
    idx+=1    
  


#reading party B Data
insertion_B=""
idx=0
for line in open(data_dir+"//party_B_Loan_Process_MPC.csv"):
    line=line.strip('\n').split(',')
    if idx==0:
        idx+=1
        continue
    
    if len(line)>1:
        line.pop(2)
        str = 'row={'+",".join(line) +'};\n'
        str+='tdbInsertRow(ds, tbl, row);\n'
        insertion_B+=str
    idx+=1    
  
script1="import shared3p;\n"
script1+="import shared3p_table_database;\n"
script1+="import stdlib;\n"
script1+="import table_database;\n"


script1+="void "
script2="() {\n"
script2+="string ds = \"DS1\";\n"
script2+=" string tbl = \""
script3="\";\n "
script3+=" tdbOpenConnection(ds);\n"
script3+="\n"
script3+=" if (tdbTableExists(ds, tbl)) {\n"
script3+="     print(\"Deleting existing table: \", tbl);\n"
script3+="     tdbTableDelete(ds, tbl);\n"
script3+=" }\n"
script3+=" print(\"Creating new table: \", tbl);\n"
script3+=" uint ncols = 9;\n"
script3+=" pd_shared3p uint vtype;\n"
script3+=" tdbTableCreate(ds, tbl, vtype, ncols);\n"

script3+=" pd_shared3p uint [[1]] row(ncols);\n"
   
script4=  "tdbCloseConnection(ds);\n"
script4+=  "}"

table_name="demo_party_A"
output=script1+" load_party_A"+script2+table_name+script3+insertion_A+script4

text_file = open(os.path.join(  os.path.dirname(os.path.dirname(__file__)) ,'demo\\demo_party_A_data.sc'), "w")
text_file.write(output)
text_file.close()


table_name="demo_party_B"
output=script1+" load_party_B"+script2+table_name+script3+insertion_B+script4

text_file = open(os.path.join(  os.path.dirname(os.path.dirname(__file__)) ,'demo\\demo_party_B_data.sc'), "w")
text_file.write(output)
text_file.close()