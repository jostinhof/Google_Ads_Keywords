# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:35:25 2019

@author: Jostin Joseph
Generating Keywords for Google Ads
 I am creating a prototype set of keywords for search campaigns for  sofas section.
 generate keywords for the following products:

    sofas
    convertible sofas
    love seats
    recliners
    sofa beds"""


# List of words to pair with products

words = ['buy', 'price', 'discount', 'promotion', 'promo','shop']

# Print list of words

for word in words:
    print(word)
    
    
    
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    # Loop through words:
    for word in words:
        # Append combinations
        keywords_list.append([product, product + ' ' + word])
        keywords_list.append([product, word + ' ' + product])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)


# Load library

import pandas as pd


# Create a DataFrame from list
keywords_df =pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it

print(keywords_df.head(100))


# Load library

import pandas as pd


# Create a DataFrame from list
keywords_df =pd.DataFrame.from_records(keywords_list)

# Print the keywords DataFrame to explore it

print(keywords_df.head(100))


# Add a campaign column
keywords_df['Campaign']='SEM_Sofas'

# Add a criterion type column
keywords_df['Criterion Type']='Exact'



# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type']='Phrase'


# Append the DataFrames
keywords_df_final = pd.concat([keywords_df,keywords_phrase],axis=0)
#keywords_df_final['Phrase']='Exact'
print(keywords_df_final.head(100))

# Save the final keywords to a CSV file
export_csv=keywords_df_final.to_csv(r'C:\Users\josti\Desktop\Datacamp\keywords.csv',index = None, header=True)

# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)


