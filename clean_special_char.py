import pandas as pd
import trans as t 
import csv

def clear_local_char_in_column(df, col_name):
    values_list = df[col_name]
    clean_values = []
    
    for val in values_list:
        clean_values.append(t.trans(str(val)))
        
    df[col_name] = clean_values
    return df


file_path = 'uk_2018_indiv.csv'

data = pd.read_csv(file_path, error_bad_lines = False,  encoding = 'utf-8', sep = ";")

print(data.head())

clear_local_char_in_column(data, "Lawyer name")
clear_local_char_in_column(data, "Global firm name")
clear_local_char_in_column(data, "Specific practice area")
clear_local_char_in_column(data, "What we said about the firm")

print("round 2")
print(data.head())

data.to_csv('legal500_uk_indiv_2018_final.csv', sep = ";")

