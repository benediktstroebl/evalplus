```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function
values = [1, 2, 3, 'abc', {}, [0]]
print(filter_integers(values))  # [1, 2, 3]
``` 
This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. The test case demonstrates the example with a list of values and prints the result.