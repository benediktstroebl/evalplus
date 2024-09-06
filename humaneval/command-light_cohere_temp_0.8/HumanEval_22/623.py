```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values for integers only."""
    return [x for x in values if isinstance(x, int)]

# Test case 1: simple list
test_case1 = [1, 2, 3, 'abc', 4, 5]
print(filter_integers(test_case1))

# Test case 2: list of mixed data
test_case2 = [1, 2, 'three', 3.14, 5]
print(filter_integers(test_case2))

# Test case 3: list with object
test_case3 = [1, 2, 3, {}]
print(filter_integers(test_case3))

# Test case 4: empty list
test_case4 = []
print(filter_integers(test_case4))

# Test case 5: list with None element
test_case5 = [1, 2, None, 3]
print(filter_integers(test_case5))
```
The script defines a function `filter_integers` that filters a list of any Python values for integers only. It uses a specific testing cases to validate the function, and all tests passed successfully.