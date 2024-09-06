```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
result1 = filter_integers(['a', 3.14, 5])
print(result1)  # Output: [5]

# Test case 2: Filter integers from a list with mixed data
result2 = filter_integers([1, 2, 3, 'abc', {}, []])
print(result2)  # Output: [1, 2, 3]

# Test case 3: Filter integers from empty list
result3 = filter_integers([])
print(result3)  # Output: []

# Test case 4: Filter integers from a list with objects
result4 = filter_integers([1, 2, '3', 4])
print(result4)  # Output: []
``` 
This code defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integers from the input. It uses the filtering technique with the `isinstance` check to achieve this.