from pyodide.http import pyfetch

endpoint = "https://www.geeksforgeeks.org/data-structures/"

response = await pyfetch(
    endpoint,
    method="GET",
)

print('FINISHED FETCH')
