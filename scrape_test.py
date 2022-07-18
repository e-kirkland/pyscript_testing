from pyodide.http import pyfetch
import asyncio

endpoint = "https://www.geeksforgeeks.org/data-structures/"

response = await pyfetch(
    endpoint,
    method="GET",
)

print('FINISHED FETCH')
