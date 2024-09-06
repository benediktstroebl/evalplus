```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list
test_case_1 = [1, 2, 3, 'abc', }  # changing data type here intentionally
print(filter_integers(test_case_1))  # Output: [1, 2, 3]

# Test case 2: Filter integers from a string
test_case_2 = "abc"  # changing data type here intentionally
print(filter_integers(test_case_2))  # Output: []

# Test case 3: Filter integers from an empty list
test_case_3 = []
print(filter_integers(test_case_3))  # Output: []
```
This script defines a function `filter_integers` that filters a given list of values, returning only the integers. The test cases provided then validate the expected output for this function.