#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

def reference1(df):
    # Filter the data for leased properties
    leased_data = df[df['Owned/Leased'] == 'LEASED']
    # Group the leased data by 'State' and count the occurrences
    leased_counts = leased_data['Bldg State'].value_counts()
    # Create a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.bar(leased_counts.index, leased_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Leased Properties by State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()

def reference2(df):
    # Filter the data for owned properties
    owned_data = df[df['Owned/Leased'] == 'OWNED']

    # Group the owned data by 'State' and count the occurrences
    owned_counts = owned_data['Bldg State'].value_counts()

    # Create a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.bar(owned_counts.index, owned_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Owned Properties by State')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot
    plt.show()

def reference3(df):
    # Filter the data for building type of properties
    building = df[df['Property Type'] == 'BUILDING']

    # Group the building data by 'State' and count the occurrences
    building_counts = building['Bldg State'].value_counts()

    # Create a bar plot using Matplotlib
    plt.figure(figsize=(20, 15))
    plt.bar(building_counts.index, building_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Property type - Building by State')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot
    plt.show()

def reference4(df):
    # Filter the data for structure type of properties
    structure = df[df['Property Type'] == 'STRUCTURE']

    # Group the structure data by 'State' and count the occurrences
    structure_counts = structure['Bldg State'].value_counts()

    # Create a bar plot using Matplotlib
    plt.figure(figsize=(20, 15))
    plt.bar(structure_counts.index, structure_counts.values, color='skyblue')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.title('Count of Property type - Structure by State')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot
    plt.show()
    
def reference5(df):
    # Group the data by 'Property Type' and calculating the average number of parking spaces
    average_spaces_by_property_type = df.groupby('Property Type')['Total Parking Spaces'].mean()

    # Create a bar plot using Matplotlib
    plt.figure(figsize=(10, 6))
    average_spaces_by_property_type.plot(kind='bar', color='lightblue')
    plt.xlabel('Property Type')
    plt.ylabel('Total Parking Spaces')
    plt.title('Total Parking Spaces by Property Type')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()
    
def reference6(df):
    import datetime as dt
    #lets calculate the age of the property using the construction date of the property
    current_date = dt.datetime.now()
    df['Property Age'] = (current_date - df['Construction Date']).dt.days // 365  # Calculate age in year
    # Print the DataFrame with the property age
    #print(df[['Construction Date', 'Property Age']])
    #df.head()
    #Group the data by 'State' and calculate the average age for each state
    average_age_by_state = df.groupby('Bldg State')['Property Age'].mean()
    # Creating a bar plot using Matplotlib
    plt.figure(figsize=(12, 6))
    average_age_by_state.plot(kind='bar', color='lightblue')
    plt.xlabel('State')
    plt.ylabel('Property Average Age')
    plt.title('Average Age of Properties by State')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # Display the plot
    plt.show()

