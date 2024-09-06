```python
from typing import List
def filter_integers(values): 
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
print(filter_integers(['a', 3.14, 5]))  # [5]

# Test case 2: Filter integers from a tuple
print(filter_integers((1, 2, 3, 'abc', {})))  # [1, 2, 3]

# Test case 3: Filter integers from an empty list
print(filter_integers([]))  # []

# Test case 4: Filter integers from a list containing other objects
print(filter_integers([1, 2, 3, 'abc']))  # [1, 2, 3]
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the values from any input, this function only adds integer values to the output.