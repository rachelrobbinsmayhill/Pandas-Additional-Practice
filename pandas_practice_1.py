# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
from lib2to3.pgen2.pgen import DFAState
import numpy as np
import pandas as pd

# MAKING DATAFRAMES
# Creating a Series by passing a list of values, letting pandas create a default integer index:
s = pd.Series([1, 3, 5, np.nan, 6, 8])
s

# Create a DataFrame by passing a NumPy array, with a datetime index and labeled columns:
dates = pd.date_range('20130101', periods = 6)
dates

DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
                '2013-01-05', '2013-01-06'],
            dtype='datetime64[ns]', freq='D')
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
df

# Create a DataFrame by passing a dict of objects that can be converted to series-like.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo"
    }
)
df2

# Observe datatypes
df2.dtypes

# View top of DF
df.head()

#View bottom of DF
df.tail()

#View index
df.index

#View columns
df.columns

# df to numpy
df.to_numpy()
df.dtypes

df2.to_numpy()
df2.dtypes

#sorting by axis
df.sort_index(axis=1, ascending=False)

#Sorting bu columns
df.sort_values(by="B")

#selecting a single column
df["A"] # select all rows, column A

#selecting specific rows
df[0:3] # select first 3 rows

#selecting by label
df
df.loc[dates[0]] #selects first row

#selecting multi-axis by label
df.loc[:,["A","B"]] #selects A and B columns with all rows

# label slicing with both endpoints included
df.loc["20130102":"20130104",["A","B"]] #selects A and B columns with rows from 20130102 to 20130104

# reducing the selection of the returned object
df.loc["20130102",["A","B"]] #selects A and B columns with row 20130102

# get a scaler value (single values):
df.loc[dates[0], "A"] #selects row 20130102, column A

# get a scaler value (fast access to rows):
df.at[dates[0], "A"] #selects row 20130102, column A

# SELECTION BY POSITION





