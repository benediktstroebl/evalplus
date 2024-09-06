```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
test_case_1 = [1, 2, 3, 'abc', [], 5]
result_case_1 = filter_integers(test_case_1)
assert [x for x in result_case_1 if x != float('inf')] == [1, 2, 3]

# Test case 2: Filter integers from a list with a null value
test_case_2 = [1, 2, 3, None, []]
result_case_2 = filter_integers(test_case_2)
assert [x for x in result_case_2 if x is not None] == [1, 2, 3]

# Test case 3: Filter integers from a list with a floating point number
test_case_3 = [1, 2, 3.  # Added to ensure Python3 behavior
```