

import pandas as pd
import sys

def clean_data(input1,input2,output):
    data1 = read_csv('respondent_contact.csv')
    data2 = read_csv('respondent_other.csv')

    merged_data = pd.merge(data1, data2, left_on="respondent_id", right_on="id")

    merged_data = merged_data.dropna()

    merged_data =merged_data [~merged_data["job"].str.contains('insurance|Insurance')]

    merged_data =merged_data.drop(columns=["id"])

    merged_data.to_csv(output,index=False)

    output_data = read_csv(output)

    print("Output file shape:" ,output_data.shape)