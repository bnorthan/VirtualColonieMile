print('hello')

import numpy as np
import pandas as pd

data=pd.read_csv('results/2020-07-17 2020 VIRTUAL COLONIE MILE Hudson Mohawk Road Runners Club.csv')

def timeToSeconds(time):
    
    temp=time.split(':')
    print(len(temp))
    try:
        if (len(temp)==2):
            return 60*int(temp[0])+int(temp[1])
        elif (len(temp)==1):
            return 60*int(temp[0])
    except:
        return 100000

data['seconds']=data['Time'].apply(lambda x: timeToSeconds(x))
data=data.drop('Event registration date',axis=1)
data=data.drop('e-Mail', axis=1)

data=data.sort_values(by='seconds')
data=data.drop('seconds',axis=1)

data=data.reset_index(drop=True)

print(data)

markdown=data.to_markdown()

fname='leaderboard.md'
out_file=open(fname, "w")
out_file.write(markdown)
out_file.close()

csvname='leaderboard.csv'
data.to_csv(csvname)

