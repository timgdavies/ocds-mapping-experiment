import json
from collections import OrderedDict

def walk(node,n = 1): 
    for key, item in node.items():
        print(type(item))

        if type(item) is OrderedDict:
            n = n + 1
            item['propertyOrder'] = n
            walk(item,n)
        else:
          #  print(item)
          pass
    return node

with open("release-schema.json", "r") as schemaFile:
    schema = json.loads(schemaFile.read(), object_pairs_hook=OrderedDict)
    
    schema = walk(schema)
    print(json.dumps(schema,indent=2))
    with open("release-schema-ordered.json","w") as outFile:
        outFile.write(json.dumps(schema,indent=2))
