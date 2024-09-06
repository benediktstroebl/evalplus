Here's the solution:
```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Basic integers
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: Strings
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]

# Test case 3: Empty list
print(filter_integers([]))  # []

# Test case 4: Lists with object elements
print(filter_integers([1, 2, 3, 'abc', {}]))  # [1, 2, 3]
```
This function takes a list of values and returns a new list containing only the integers from the input. It uses the necessary to convert all values to integers, and the isinstance function to check if each value is an integer. 

The test cases cover basic scenarios, empty lists, strings, and lists with objects. The expected output matches the results.