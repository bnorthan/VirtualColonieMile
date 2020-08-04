print('hello')

import numpy as np
import pandas as pd

sys.path.append('../scoreware-site/util/runner/')
import runnerutils

data=pd.read_csv('results/2020-08-03 2020 VIRTUAL COLONIE MILE Hudson Mohawk Road Runners Club.csv')

def timeToSeconds(time):
    temp=time.split('.') 
    temp=temp[0].split(':')
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

data.index+=1

print(data)

markdown=data.to_markdown()

fname='leaderboard.md'
out_file=open(fname, "w")
out_file.write(markdown)
out_file.close()

csvname='leaderboard.csv'
data.to_csv(csvname)

data.Gender=data.Gender.apply(lambda x: x.lower())
data.Gender=data.Gender.apply(lambda x: x[0])

data["age_cat"]=data.Age.apply(lambda x:runnerutils.ageToCat_0_80_10(x))

age_cats=['0_9','10_19','20_29','30_39','40_49','50_59','60_69','70_79','80+']

females=data[data.Gender=='f']
males=data[data.Gender=='m']

age_markdown='';

for age in age_cats:
    age_markdown+='## Female '+age+'  \n\n'
    temp=females[females.age_cat==age]
    
    temp=temp.drop('age_cat',1)
    if (temp.shape[0]>0):
        age_markdown+=temp.to_markdown()+'  \n\n'
    else:
        age_markdown+='  \n\n'
        
    age_markdown+='## Male '+age+'  \n\n'
    temp=males[males.age_cat==age]
    
    temp=temp.drop('age_cat',1)
    if (temp.shape[0]>0):
        age_markdown+=temp.to_markdown()+'  \n\n'
    else:
        age_markdown+='  \n\n'
    
'''
temp=females[females.age_cat=='30_39']
age_markdown=''
age_markdown+='## Females2\n\n'
age_markdown+=temp.to_markdown()    
'''
 
out_file=open('age.md', "w")
out_file.write(age_markdown)
out_file.close()


    




