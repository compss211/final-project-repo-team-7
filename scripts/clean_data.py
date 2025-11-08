'''
The code to clean the all_speeches.csv

#Cleaning
#To do:
#remove audio and video
#lowercase and clean Transcripts
'''
import pandas as pd
import numpy as np
import re


def clean_text(text):
    '''
    Cleans the text transcripts
    '''
    import pandas as pd 
    import re

    #Deals w/ empty transcripts
    if pd.isna(text):
        return ""
    
    #make lowercase
    text = text.lower()

    #remove white space, special characters
    text = text.strip()
    text = re.sub(r'[^a-zA-Z0-9]', '', text)

    #prevents double spaces
    text = text.replace('  ', ' ')

    #set and return
    cleaned = text  # placeholder
    
    return cleaned

def tokenize(df):
    return