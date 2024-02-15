

import pandas as pd
import sys

def clean_data(input1,input2,output):
    data1 = pd.read_csv('respondent_contact.csv')
    data2 = pd.read_csv('respondent_other.csv')

    merged_data = pd.merge(data1, data2, left_on="respondent_id", right_on="id")

    merged_data = merged_data.dropna()

    merged_data =merged_data [~merged_data["job"].str.contains('insurance|Insurance')]

    merged_data =merged_data.drop(columns=["id"])

    merged_data.to_csv(output,index=False)

    output_data = pd.read_csv(output)

    print("Output file shape:" ,output_data.shape)

if __name__ == "__main__":
    input_file1 = "respondent_contact.csv"
    input_file2 = "respondent_other.csv"
    output_file = "output.csv"

    clean_data(input_file1, input_file2, output_file)