import pandas as pd
import settings as s
from Strangers import Stranger


df = pd.read_excel(s.old_cms)

def create_members(df):
    Members = df.iloc[:,:4]
    Members = Members.drop_duplicates()
    return Members

def match_list(df):
    df_melted = pd.melt(df, id_vars=['KP email'], value_vars=s.prev_matches, 
                        var_name='Month', value_name='Matches')
    
    df_melted['Matches'].fillna('No match found', inplace=True)

    # Group by 'KP email' and count occurrences of each match
    grouped = df_melted.groupby('KP email')['Matches'].value_counts().unstack(fill_value=0)

    # Create a list of dictionaries for each unique KP email
    result = {}

    for kp_email, row in grouped.iterrows():
        matches_dict = row[row > 0].to_dict()  # Convert only non-zero counts to a dictionary
        result[kp_email] = matches_dict
        
    return result


def Create_Strangers(df):
    
    Strangers = []
    
    for index, row in df.iterrows():
        stranger = Stranger(row['KP email'], row['First name'], row['Last name'], row['Team'])
        Strangers.append(stranger)
    
    return Strangers


def appending_prev_matches(Strangers, matches):
    
    updated_list = []
    
    for stranger in Strangers:
        prev_matches = matches['stranger.kp_email']
        stranger.previous_matches = prev_matches
        updated_list.append(stranger)
    
    return updated_list