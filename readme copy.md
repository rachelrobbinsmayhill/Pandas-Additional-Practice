# Visualization Warmup

1. Copy the following code into a jupyter notebook named `visualization_warmup.ipynb`

    ```python
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np

    url = 'https://gist.githubusercontent.com/zgulde/018f5d601efc79cb741a7aba92f51d29/raw/c08f1c09f605b43e9a354890f9dd68f296e76dc4/students.csv'
    df = pd.read_csv(url)
    ```

1. `df` contains (fake) data on students time at codeup:

    - `ml_coffee`: coffee consumption in milliliters
    - `syntax_errors`: number of syntax errors
    - `p_days_absent`: percentage of days absent
    
1. Create a scatter plot of `syntax_errors` and `ml_coffee`. Make sure to give your visual an appropriate title and labels.

1. Create a scatter plot of `p_days_absent` and `ml_coffee`. Make sure to give your visual an appropriate title and labels.

1. Perform any other customizations you think will help to the plots you have created