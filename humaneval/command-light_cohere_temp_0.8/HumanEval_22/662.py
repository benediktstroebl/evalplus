```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
test_case_1 = [1, 2, 3, 'abc', [], 5]
print(filter_integers(test_case_1))
# [1, 2, 3]

# Test case 2: Filter integers from a list of any data types
test_case_2 = ['a', 3.14, 5]
print(filter_integers(test_case_2))
# [3.14, 5]
```