import json
import requests
import pandas as pd

def lambda_handler(event,context):
    print('event data ->', event)
    response=response.get("https://www.google.com/")
    print(response.text)

    d={'col1':[1,2,3],'col2':[4,5,6]}
    df=pd.DataFrame(data=d)
    print(df)
    print('Done x1.1')
    print('demo completed !!!')