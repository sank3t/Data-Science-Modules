# Modules for performing data cleaning and descriptive stats
import re
import pandas as pd

def rename_columns(columns: list):
    columns = ['_'.join(re.sub('[.-]', '_', col).strip().lower().split()) for col in columns]
    return columns


def unique_value_count(df: pd.DataFrame):
    df_nunique = df.nunique().reset_index()
    df_nunique['dtype'] = df.dtypes.reset_index().loc[:, 0]
    df_nunique.columns = ['column', 'nunique', 'dtype']
    
    display(df_nunique)


def missing_value_stats(df: pd.DataFrame):
    """
        Considering the count of NaN points only
    """
    num_rows = df.shape[0]
    # Missing value count by columns
    df_missing = df.isna().sum().reset_index()
    # Renaming columns
    df_missing.columns = ['column', 'missing_values']
    # Getting only those columns having missing values > 0
    df_missing = df_missing[df_missing['missing_values'] > 0]
    df_missing.reset_index(drop=True, inplace=True)
    # Calculating percentage of missing
    df_missing['missing_percentage'] = df_missing['missing_values'].apply(
        lambda missing_value: round((missing_value / num_rows) * 100, 2)
    )

    if df_missing.shape[0] > 0:
        display(df_missing)
    else:
        return "The dataset has no NaNs"


def get_value_counts(
    df: pd.DataFrame,
    is_normalized=True
):
    """
        Getting the value counts of columns
    """
    for col in df.columns:
        print(col)
        print(df[col].value_counts(normalize=is_normalized))
        print("-"*50)
