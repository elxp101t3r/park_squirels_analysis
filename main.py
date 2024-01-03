import pandas as pd

class Data:
    def __init__(self, file_name):
        self.file = file_name
    
    def r_csv(self):
        self.data = pd.read_csv(f'{self.file}')
    
    def convert_to_df(self):
        self.colors_dict = {
            'Fur Color': ['Red', 'Gray', 'Black'],
            'Count': [
                sum(self.data['Primary Fur Color'] == 'Cinnamon'),
                sum(self.data['Primary Fur Color'] == 'Gray'),
                sum(self.data['Primary Fur Color'] == 'Black')
            ]
        }
        self.df = pd.DataFrame(self.colors_dict)
    
    def create_the_csv(self):
        self.df.to_csv('colors_csv.csv')
        

data = Data('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240103.csv')

data.r_csv()
data.convert_to_df()
data.create_the_csv()      
