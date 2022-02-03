import pandas as pd
import json

def map_schema(schema):
    schema_updated = {}
    for key,value in schema.items():
        if schema[key] == 'STRING':
            schema_updated[key] = 'object'
        elif schema[key] == 'DATE':
            schema_updated[key] = 'datetime64'
        elif schema[key] =='TIME':
            schema_updated[key] = 'datetime64'
        elif schema[key] == 'INTEGER':
            schema_updated[key] = 'int64'
        elif schema[key] == 'FLOAT':
            schema_updated[key] = 'float64'
    return schema_updated

filename = input("Enter filename to validate: ")
#schemafile = input("Enter schema to validate: ")

#filename = 'SAP_FI_YMFAT_JVBKPFDASH_YMFAT_JVBKPFDASH_2020-07-17 12_43_39.csv'
schemafile = 'schema.txt'

# read schema file

with open('schema.txt') as schemafile:
    schema = json.loads(schemafile.read())

# mapping schemafile
schema_mapped = map_schema(schema)

# read csv file
df = pd.read_csv(filename,delimiter='|')

#checking column counts

print("columns in csv file:",len(list(df.columns)))
print("columns in schema",len(schema))

# checking columns to see if they match

missing_cols =[]

for col in schema:
    if col not in list(df.columns):
        missing_cols.append(col)
print("missing/mismatched columns:", missing_cols)

# casting datatype to check for errors
error_columns = []

try:
 for key,value in schema_mapped.items():
   try:
     df[key].astype(value)
   except:
     print("Error in column {} it has datatype {} should have {} ".format(key, df[key].dtype,value))
     error_columns.append(key)
 print("All datatypes matched!")
 print("Error columns :", error_columns)
except:
    print("Not matching column datatype, resolve earlier errors")












