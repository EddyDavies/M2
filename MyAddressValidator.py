import sys
import json
from jsonschema import validate


def validate_address(address_file_path):
#     """This function validates the input JSON ﬁle against your 
#        schema and returns 
#             "yes" 
#        if your addresses contain a large household (as per M1), 
#             "no" 
#        otherwise, and that uses the JSON Schema validator 
#        documented at 
#            https://python-jsonschema.readthedocs.io/en/stable/validate/ 
#        to validate the input against your schema. In case this validation 
#        fails, your program should return 
#             "invalid". 

#      You can use "pip install jsonschema" to install jsonschema."""

     x = address_file_path.rfind('/') 
     schema_file_path = address_file_path[:x+1] + "address.json.schema"

     schema = open(schema_file_path, "r").read()
     expr = open(address_file_path, "r").read()


     jsonSchema = json.loads(schema)
     jsonData = json.loads(expr)

     try:
          validate(instance=jsonData, schema=jsonSchema)
     except jsonschema.exceptions.ValidationError as err:
          # print("Given JSON data is InValid")
          return "invalid"
     else:
          pass
          # print("Given JSON data is Valid")

     address_list = []
     for person in jsonData:
          counted = False
          for address in address_list:
               if person["address"] is address["address"]:
                    address["count"] += 1
                    counted = True
               if address["count"] >= 3:
                    return "yes"
          if not counted:
               address_list.append({
                    "address" : person["address"],
                    "count" : 1
               })
     
     return "no"

if __name__=='__main__':
#     address_file_path = sys.argv[1]
#     print(validate_address(address_file_path))

     files = [
    "/Users/edwarddavies/Documents/UoM/_Modelling Data/M2/ValidNoLarge.json",
    "/Users/edwarddavies/Documents/UoM/_Modelling Data/M2/ValidSomeLarge.json",
    "/Users/edwarddavies/Documents/UoM/_Modelling Data/M2/Invalid3.json"
     ]

     for file in files:
          print(validate_address(file))