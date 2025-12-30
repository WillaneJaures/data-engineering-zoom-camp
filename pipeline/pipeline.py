import sys
import pandas as pd 


df = pd.DataFrame({"day": [1,2], "pass_numb": [3,4], "momth": [12,12]})


print(df.head())
df.to_parquet(f"output.parquet")