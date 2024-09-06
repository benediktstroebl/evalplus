```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test the function with some examples
values1 = [1, 2, 3, 'abc', {}, [5], [0] ]
values2 = [3.14, 5]
print("Test 1:")
print(filter_integers(values1))  # Output: [1, 2, 3]
print("Test 2:")
print(filter_integers(values2))  # Output: [5]
```

This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the specific typing to ensure that only elements of type `int` are included.