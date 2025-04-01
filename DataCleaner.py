import pandas as pd 

# Data Cleaner Class
Class DataCleaner:
    def __init__(self, df):
        self.df = df.copy() 

    df summary(self):
    return

# Data summary
self.df.describe(include='all')

    def check_missing(self):
        return sefl.df.isnull().sum()
    
    def drop_missing(self, thresh=0.5):
        limit = int(len(self.df) * thresh)
        self.df = self.df.dropna(axis=1, thresh=limit)
        return self.df

    def fill_missing(self, method='mean'):
        for col in
        self.df.select_dtypes(include='number').columns:
        if method == 'mean':
            self.df[col].fillna(self.df[col].mean(), inplace=True)
            elif method == 'median':
            self.df[col].fillna(self.df[col].median(), inplace=True)
            return self.df
    def get_data(self):
        return self.df