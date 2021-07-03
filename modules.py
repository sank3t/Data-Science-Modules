# Modules for performing descriptive stats

def unique_value_count(df):
    df_nunique = df.nunique()
    df_nunique = df_nunique.rename(
        columns={"index": "columns", 0: "nunique"}
    )

    return df_nunique


def missing_value_stats(df):
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
        return df_missing
    else:
        return "The dataset has no NaNs"
