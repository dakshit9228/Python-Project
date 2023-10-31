# data_summary.py

import pandas as pd
import numpy as np

class DataSummary:
    def __init__(self, data_url):
        """
My data has 18 columns and 8770 rows of data.

** Attributes : **

Location Code : location code

Region Code ; region code of building

Bldg Address1 : address of building

Bldg Address2 : address of building

Bldg City :city of building

Bldg County :county of building

Bldg State :state of building

Bldg Zip :ZIP code of building

Congressional District :District of building

Bldg Status :Status of building

Property Type :TYpe of properTY

Bldg ANSI Usable :Ansi usable

Total Parking Spaces :Parking spaces

Owned/Leased :Leased or Owned

Construction Date : Date of bulding construction

Historical Type : Historical type

Historical Status : Historical Status

ABA Accessibility Flag : Flag
        """
        self.data_url = data_url

    def fetch_data(self):
        """
        Fetch data from the specified URL.

        Returns:
            pd.DataFrame: The fetched DataFrame.
        """
        try:
            df = pd.read_csv(self.data_url)
            return df
        except Exception as e:
            return None

    def display_data_info(self, df):
        """
        Display information about the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to display information for.
        """
        print("Sample data:")
        print(df.head())
        print("Data shape:", df.shape)
        print("Data information:")
        print(df.info())