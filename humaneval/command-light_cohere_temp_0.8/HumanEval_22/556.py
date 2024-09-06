```python
from typing import List

def filter_integers(values):
    """Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test case 1
values_test1 = ['a', 3.14, 5]
print(filter_integers(values_test1))  # Output: [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
print(filter_integers(values_test2))  # Output: [1, 2, 3]

# Test case 3
values_test3 = [1, 2, 3, []]
print(filter_integers(values_test3))  # Output: [1, 2, 3]
```
The function `filter_integers` is self-contained and solves the problem of filtering out integers from a given list of any python values. It successfully passes all tests and can be easily modified to solve other related problems.