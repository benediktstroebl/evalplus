```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test cases
values1 = [1, 2, 'three', 'five', (6), [7])
values2 = [1, 2, 'three', (123), [456])

print("Test case 1:")
print(filter_integers(values1))

print("Test case 2:")
print(filter_integers(values2))
```
This script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. It uses the specific typing to ensure that only the appropriate types of values are accepted.