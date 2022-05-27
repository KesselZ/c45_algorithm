import pandas as pd
def is_number(string):
    for i in range(0, len(string)):
        if pd.isnull(string[i]) == False:          
            try:
                float(string[i])
                return True
            except ValueError:
                return False

