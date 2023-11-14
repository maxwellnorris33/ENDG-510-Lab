import pandas as pd # in case of error, install pnadas using: pip install pandas
import random
# Read the CSV file into a DataFrame
df = pd.read_csv('cool_af_data.csv')
for i in range(300):
    new_data = {
        'Temp': random.uniform(0,200),
        'Humd': random.uniform(0,100),
        'Label': 0
        }
    df = df.append(new_data, ignore_index=True)
# Step 3: Save the DataFrame to a new CSV file
df.to_csv("data_the_sequel.csv", index=False)