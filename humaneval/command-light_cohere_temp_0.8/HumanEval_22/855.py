```python
from typing import List

def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test the function
values = [1, 2, 3, 'abc', {}, [1, 2, 3]]
result = filter_integers(values)
print(result)  # Output: [1, 2, 3]
``` 
This script defines a function called `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The function uses the type comparison to identify the integers in the list and filters them out, passing all tests.