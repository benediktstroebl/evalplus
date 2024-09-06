```python
from typing import List

def filter_integers(values):
    return [int(i) for i in values if type(i) == int]

# Test case 1: Filter integers from a list
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: Filter integers from a list with other data types
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3: Filter integers from an empty list
print(filter_integers([]))        # []
```
The code defines a function **filter_integers** that accepts a list of any value and returns a new list containing only the integers from the input. The code passes three test cases, successfully filtering integers from a list of various types of data.

The output of the code is: [5]