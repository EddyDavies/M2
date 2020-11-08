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
    
     with open(schema_file_path, "r") as schema:
          with open(address_file_path, "r") as expr:

               jsonData = json.load(expr)
               jsonSchema= json.load(schema)
               print(json.dumps(jsonData, indent=4))

               try:
                    validate(instance=jsonData, schema=jsonSchema)
               except jsonschema.exceptions.ValidationError as err:
                    print("Given JSON data is InValid")
               else:
                    print("Given JSON data is Valid")

     pass

if __name__=='__main__':
#     address_file_path = sys.argv[1]
#     print(validate_address(address_file_path))

     files = [
    "/Users/edwarddavies/Documents/UoM/_Modelling Data/M2/ValidNoLarge.json",
#     "/Users/edwarddavies/Documents/UoM/_Modelling Data/M2/ValidSomeLarge.json",
#     "/Users/edwarddavies/Documents/UoM/_Modelling Data/M2/Invalid3.json"
     ]

     for file in files:
          print(validate_address(file))