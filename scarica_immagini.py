import time

from PIL import Image
import requests

import json

# Opening JSON file
f = open('21_32.json')

# returns JSON object as
# a dictionary
data = json.load(f)
file_da_modificare=data['DocumentStream'][0]
# Iterating through the json
# list


# Closing file
f.close()

data['DocumentStream'][0]['_id']#lavoriamo solo sul primo [0]

data['DocumentStream'][0]['_id']='8056597444484'
data['DocumentStream'][0]['moco']='0RW4002__63258750'
data['DocumentStream'][0]['model']='0RW4002'

url='https://smartshopper-im.luxottica.com/'

folder="/TestSTG/RW/0RW4002__63258750"
filename = '0RW4002__63258750'

res=data['DocumentStream'][0]['pictures_flags']
for i in data['DocumentStream'][0]['pictures']['Catalog image']:
    data['DocumentStream'][0]['pictures']['Catalog image'][i]
    # 'https://smartshopper-im.luxottica.com/RB/0RB2132/0RB2132__622.jpg']
    try:
        time.sleep(5)
        path=url+data['DocumentStream'][0]['pictures']['Catalog image'][i][0]
        print(path)
        im = Image.open(requests.get(path, stream=True).raw)
        data['DocumentStream'][0]['pictures']['Catalog image'][i][0]=folder+filename+path.split('__')[-1]#cambio il nome del file ed il nome nel json
        #im.filename =
        #im.save#(i.split('/')[-1].replace('"','hhhh'),"PNG")
        im.save(filename+path.split('__')[-1])
    except:
        data['DocumentStream'][0]['pictures']['Catalog image'][i][0] = ''
        print('scoppiato')

        pass


for i in data['DocumentStream'][0]['pictures']['Degree']:
    try:
        time.sleep(5)
        path=url+data['DocumentStream'][0]['pictures']['Degree'][i][0]
        print(path)

        im = Image.open(requests.get(path, stream=True).raw)
        im.save(filename+path.split('__')[-1])
        data['DocumentStream'][0]['pictures']['Degree'][i][0]=folder+filename+path.split('__')[-1]

    except:
        data['DocumentStream'][0]['pictures']['Degree'][i][0]=''
        print('scoppiato')

        pass


for i in data['DocumentStream'][0]['pictures']['PI20']:
    for n, elem in enumerate(data['DocumentStream'][0]['pictures']['PI20'][i]):
        data['DocumentStream'][0]['pictures']['PI20'][i][n]=elem
        try:
            time.sleep(5)
            path = url + data['DocumentStream'][0]['pictures']['PI20'][i][n]
            print(path)

            im = Image.open(requests.get(path, stream=True).raw)
            im.save(filename + '_'+path.split('__')[-2]+'_'+path.split('__')[-1])
            data['DocumentStream'][0]['pictures']['PI20'][i][n]=folder+filename + '_'+path.split('__')[-2]+'_'+path.split('__')[-1]

        except:
            data['DocumentStream'][0]['pictures']['PI20'][i][n]=''
            print('scoppiato')
            pass



#for i in data['DocumentStream'][0]['pictures']:
res=data['DocumentStream'][0]
json_object = json.dumps(res, indent = 4)
print(json_object)
