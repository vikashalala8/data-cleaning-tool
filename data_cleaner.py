import numpy as np
import pandas as pd


# Function for cleaning missing values
def clean(file_path):

    # Read CSV file
    df1 = pd.read_csv(file_path)

    # Loop through each column
    for col in df1.columns:

        # Count missing values
        missing_values = df1[col].isnull().sum()

        # Check if missing values exist
        if missing_values > 0:

            # For integer columns
            if df1[col].dtype == 'int64':

                mean_value = df1[col].mean()

                df1[col] = df1[col].fillna(mean_value)

            # For float columns
            elif df1[col].dtype == 'float64':

                mean_value = df1[col].mean()

                df1[col] = df1[col].fillna(mean_value)

            # For object/string columns
            elif df1[col].dtype == 'object':

                mode_value = df1[col].mode()[0]

                df1[col] = df1[col].fillna(mode_value)

        else:
            print(f"No missing values found in column: {col}")

    return df1
