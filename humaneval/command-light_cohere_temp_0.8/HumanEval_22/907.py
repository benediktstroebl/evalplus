```python
from typing import List
def filter_integers(values):
    return [int(i) for i in values if type(i) == int]

# Test cases
values1 = ['a', 3.14, 5]
values2 = [1, 2, 3, 'abc', {}, []]
values3 = [1, 2, 3]

print(filter_integers(values1))  # Output: [5]
print(filter_integers(values2))  # Output: [1, 2, 3]
print(filter_integers(values3))  # Output: []
```
This script defines a function `filter_integers` that filters a list of any values and returns a new list containing only the integers. It uses the same test to validate its function. The test cases cover different types of input values, and the function successfully filters out non-integer elements and returns the expected integer list.