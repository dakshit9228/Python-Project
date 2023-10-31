# eda.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

class EDA:
    def __init__(self, data):
        """
        Initialize the EDA class with a DataFrame.

        Args:
            data (pd.DataFrame): The input DataFrame.
        """
        self.data = data

    def drop_columns(self):
        """
        Drop columns that are not required.

        Returns:
            pd.DataFrame: The DataFrame with columns dropped.
        """
        columns_to_drop = ['Location Code', 'Region Code', 'Bldg Address1', 'Bldg Address2', 'Bldg Zip', 'Congressional District',
                           'Bldg ANSI Usable', 'Historical Type', 'Historical Status', 'ABA Accessibility Flag ']
        self.data = self.data.drop(columns=columns_to_drop, axis=1)
        return self.data
    
    def handle_date_column(self):
        """
        Convert the 'Construction Date' column to a datetime data type.

        Returns:
            pd.DataFrame: The DataFrame with the date column converted.
        """
        self.data['Construction Date'] = self.data['Construction Date'].replace('1/0/1900', '1/1/1900')
        self.data['Construction Date'] = pd.to_datetime(self.data['Construction Date'])
        return self.data

    def create_date_attributes(self):
        """
        Create day, month, and year attributes from the 'Construction Date' column.

        Returns:
            pd.DataFrame: The DataFrame with date attributes added.
        """
        self.data['Day'] = self.data['Construction Date'].dt.strftime('%A')
        self.data['Month'] = self.data['Construction Date'].dt.strftime('%B')
        self.data['Year'] = self.data['Construction Date'].dt.year
        return self.data

    def generate_summary_statistics(self):
        """
        Generate summary statistics for the DataFrame.

        Returns:
            pd.DataFrame: Summary statistics.
        """
        return self.data.describe()

    def plot_box_plot(self):
        """
        Create a box plot for the DataFrame.

        Returns:
            None
        """
        plt.figure(figsize=(8, 8))
        sns.set(style="whitegrid")
        ax = sns.boxplot(data=self.data, orient="v", palette="Set1")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)  # Rotating labels
        plt.tight_layout()
        plt.show()

    def plot_top_cities(self):
        """
        Create bar plots to visualize the top 5 cities by count using both Matplotlib and Seaborn.

        Returns:
            None
        """
        top_cities = self.data['Bldg City'].value_counts().head(5)

        # Create a bar plot using Seaborn
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_cities.index, y=top_cities.values, palette='viridis')
        plt.xlabel('City')
        plt.ylabel('Count')
        plt.title('Top 5 Cities by Count')
        plt.xticks(rotation=45)  # Rotate city labels for better readability
        plt.tight_layout()
        plt.show()

        # Create a bar plot using Matplotlib
        plt.figure(figsize=(10, 6))
        plt.bar(top_cities.index, top_cities.values, color='skyblue')
        plt.xlabel('City')
        plt.ylabel('Count')
        plt.title('Top 5 Cities by Count')
        plt.xticks(rotation=45)  # Rotate city labels for better readability
        plt.tight_layout()
        plt.show()
        
    