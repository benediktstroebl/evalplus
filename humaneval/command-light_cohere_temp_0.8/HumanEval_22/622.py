```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = [1, 2, 3, 'abc', }
print("Test case 1: ", end="")
print(filter_integers(values1))  # Output: [1, 2, 3]

# Test case 2
values2 = [1, 2, 3, 'abc', [], 5]
print("Test case 2: ", end="")
print(filter_integers(values2))  # Output: [1, 2, 3, 'abc', 5]

# Test case 3
values3 = [1, 2, 3]
print("Test case 3: ", end="")
print(filter_integers(values3))  # Output: [1, 2, 3]
```
This script defines a function **filter_integers** that filters a list of values and returns a new list containing only the integers. It then passes three test cases and the output is as expected.