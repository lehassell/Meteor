import pandas as pd

data = pd.read_csv('C:\Users\Ed\Documents\Datasets\Meteorite_Landings.csv')

print data.head()
print data.describe()

#so mass is in grams.  As an American this feels horribly unintuitive and so I will convert to lbs

data['mass_lbs'] = data['mass (g)'] /.0022
print data['mass_lbs'].describe()