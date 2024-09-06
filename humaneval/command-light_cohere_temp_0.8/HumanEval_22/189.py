```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of input
values_test = [
    [],  # [] converts to () which is considered as empty set, hence all elements are integers
    ['a', 3, 'four', (5)] ,
    [1, 2, 'three', 3],
    [True, 'string']
]

print("Results of filtering integers:")
[x for x in filter_integers(values_test)]
``` 
This script defines a function `filter_integers` that filters a list of any values and returns a new list containing only the integers. The function uses the particular values in the `values_test` list and prints the results.