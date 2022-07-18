import json
from pyodide import to_js
import js
from js import Object

request_params = {
    "method": "GET",
}
req = await js.fetch('geeksforgeeks.org/data-structures/', 
    to_js(request_params, dict_converter=js.Object.fromEntries)
)
res = await req.json()
stringResult = js.JSON.stringify(res)
print("STRING RESULT: ", stringResult)
print("FINISHED")
