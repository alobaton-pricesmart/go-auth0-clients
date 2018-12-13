import json
import os

swagger = None

for filename in os.listdir("./swagger"):
    component = json.load(open(os.path.join("swagger", filename)))

    if not swagger:
        swagger = component
    else:
        swagger['paths'].update(component['paths'])
        swagger['definitions'].update(component['definitions'])

# Pach to https://community.auth0.com/questions/9720/discrepancy-between-the-resource-server-api-respon
for t in ['get_resource-servers_by_id_response', 'get_resource-servers_response']:
    x = swagger['definitions'][t]['properties']
    x['id'] = {"description": "The id of the resource server.", "type": "string"}
    x['name'] = {"description": "The name of the resource server.", "type": "string"}

json.dump(swagger, open("swagger.json", "w"))