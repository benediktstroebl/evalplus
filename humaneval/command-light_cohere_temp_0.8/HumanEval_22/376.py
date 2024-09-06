```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [num for num in values if isinstance(num, int)]

# Test cases for function
values1 = [1, 2, 3, 'abc', [], 5]
values2 = [3.14, 'abc', None, 7, 9. massive, 10, 'invalid']

print(f"Case 1: Result: {value for values1} = {filter_integers(values1)}")  # [1, 2, 3]
print(f"Case 2: Result: {value for values1} = {filter_integers(values2)}")  # [3.14, 'abc', None, 7, 9]
```