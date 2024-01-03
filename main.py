import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240103.csv')
color_dict = {
    'Fur Color': ['Red', 'Gray', 'Black'],
    'Count': [
        sum(data['Primary Fur Color'] == 'Cinnamon'),
        sum(data['Primary Fur Color'] == 'Gray'),
        sum(data['Primary Fur Color'] == 'Black')
    ]
}
df = pd.DataFrame(color_dict)
df.to_csv('colors_csv.csv')
