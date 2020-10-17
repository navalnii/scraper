import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import timeit

start = timeit.default_timer()



def list_emp(user, st_date, end_date):
    root = ET.parse('test.xml')
    name = []
    start_time = []
    end_time = []

    for type_tag in root.findall('people'):
        name.append(type_tag.get('full_name'))
        start_time.append(type_tag.find('start').text)
        end_time.append(type_tag.find('end').text)

    df = pd.DataFrame(list(zip(name, start_time, end_time)),columns=['name', 'start_time', 'end_time'])
    df.start_time = pd.to_datetime(df.start_time)
    df.end_time = pd.to_datetime(df.end_time)
    df['diff_time'] = df.end_time-df.start_time
        
    if user == '':
        if st_date == '' and end_date == '':
            return df            
            
        elif st_date == '' and end_date != '':
            res = df[(df['end_time'] < datetime.strptime(end_date, '%Y-%m-%d'))]
            return res
            
        elif st_date != '' and end_date == '':
            res = df[(df['start_time'] > datetime.strptime(st_date, '%Y-%m-%d'))]
            return res
        
        else:
            res = df[(df['start_time'] > datetime.strptime(st_date, '%Y-%m-%d')) \
                        & (df['end_time'] < datetime.strptime(end_date, '%Y-%m-%d'))]
            return res 
            
    else:
        if st_date != '' and end_date != '':
            res = df.loc[df['name'] == user]
            res = res[(res['start_time'] > datetime.strptime(st_date, '%Y-%m-%d')) \
                        & (res['end_time'] < datetime.strptime(end_date, '%Y-%m-%d'))]
            return res
            
        elif st_date != '' and end_date == '':
            res = df.loc[df['name'] == user]
            res = res[(res['start_time'] > datetime.strptime(st_date, '%Y-%m-%d'))]
            return res
            
        elif st_date == '' and end_date != '':
            res = df.loc[df['name'] == user]
            res = res[(res['end_time'] < datetime.strptime(end_date, '%Y-%m-%d'))]
            return res
            
        else:
            res = df.loc[df['name'] == user]
            return res
            
    return df
   

if __name__ == '__main__':
    res = list_emp('i.ivanov', '2011-01-01','') #list_emp('i.ivanov', '2011-01-01','2011-12-05')
    #print(res)
    stop = timeit.default_timer()

    print('Time: ', stop - start)  

    