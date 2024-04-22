from faker import Faker
import numpy as np
import pandas as pd

Faker.seed(0)
fake = Faker()

primary_normal = np.random.normal(
                    loc = 18000,
                    scale = 1000,
                    size = 25000
                )

secondary_normal = np.random.normal(
                    loc = 22000,
                    scale = 1000,
                    size = 25000
                )

tertiary_normal = np.random.normal(
                    loc = 30000,
                    scale = 1000,
                    size = 25000
                )

def generate_df(length_df:int) -> pd.DataFrame:
    
    dict = {
        'first name': [],
        'last name': [],
        'job': [],
        'studies': [],
        'salary': []
    }
    
    for _ in range(int(length_df)):
        
        dict['first name'].append(fake.first_name())
        dict['last name'].append(fake.last_name())
        dict['job'].append(fake.job())
        studies = np.random.choice(
            a = ['primary', 'secondary', 'tertiary'],
            replace = True,
            p = [0.6, 0.25, 0.15]
        )
        
        match studies:
            
            case 'primary':
                salary = np.random.choice(primary_normal)
            case 'secondary':
                salary = np.random.choice(secondary_normal)
            case 'tertiary':
                salary = np.random.choice(tertiary_normal)
                
        dict['studies'].append(studies)
        dict['salary'].append(salary)
        
    return pd.DataFrame(dict)
    
if __name__ == '__main__':
    
    length_df = input('Please insert length of a DataFrame: ')
    df = generate_df(length_df = length_df)
    
    path = input('Please insert path: ')
    CSV_PATH = path.replace('"', '') + r'\faker-gen.csv'
    
    try:
        df.to_csv(CSV_PATH)
        print(f'DataFrame csv ({len(df)} rows) generated successfully on path {CSV_PATH}.')
    
    except:
        print('Unable to generate DataFrame csv. Check Path')