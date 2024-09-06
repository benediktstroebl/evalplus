```python
from typing import List
def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [element for element in values if type(element) == int]

# Test cases
test_values = [
    [],  # [] is empty, should return []
    ['a', 3, 'c'],  # Contains non-integer value
    [1, 2, 'three'],  # Contains duplicate integer
]

test_cases = [test_values, test_values[::-1]]

print(filter_integers(test_cases))  # Output: [1, 2, 'three']
```