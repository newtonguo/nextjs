import os
import json

products =[]

for dirname, _, filenames in os.walk('./fan'):
    folder_name = os.path.basename(dirname)
    data = {"name":"",
            "images":[],
            "type":"fan",
            "url":""}
    for filename in filenames:
        data["images"].append((os.path.join("assets/img/s-product/fan",folder_name, filename)).replace("\\", "/"))
        data["name"]=folder_name
        data["type"]="fan"
        data["url"]="product-details-fan.html?name="+folder_name + "&imgs="+str(data["images"])
    products.append(data)


for dirname, _, filenames in os.walk('./pad'):
    folder_name = os.path.basename(dirname)
    data = {"name":"",
            "images":[],
            "type":"fan",
            "url":""}
    for filename in filenames:
        data["images"].append((os.path.join("assets/img/s-product/pad",folder_name, filename)).replace("\\", "/"))
        data["name"]=folder_name
        data["type"]="pad"
        data["url"]="product-details-pad.html?name="+folder_name + "&imgs="+str(data["images"])
    products.append(data)

# for dirname, _, filenames in os.walk('./pad'):
#     folder_name = os.path.basename(dirname)
#     data[folder_name] = {
#         "name": folder_name,
#         "images": []
#     }
#     for filename in filenames:
#         data[folder_name]["images"].append(os.path.join(dirname, filename))

with open('data.json', 'w') as f:    
    json.dump(products, f)  