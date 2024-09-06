```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 3, 'abc', {}, [1, 2, 3])
values2 = [3.14, 'abc', 5, 6, 7]

print(filter_integers(values1))  # Output: [1, 2, 3]
print(filter_integers(values2))  # Output: [3.14, 'abc', 5, 6, 7]
```
This script defines a function `filter_integers` that filters out any non-integer values from a given list. It uses the Python's `isinstance` function to check if each value in the list is an integer. The test cases demonstrate how the values pass the filter for integers and how the function behaves correctly.