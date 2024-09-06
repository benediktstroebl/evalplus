```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
test_case_1 = ['a', 3.14, 5]
result_test_case_1 = filter_integers(test_case_1)
assert result_test_case_1 == [5], "Test case 1 failed"

# Test case 2: Filter integers from a list of items
test_case_2 = [1, 2, 3, 'abc', {}, []]
result_test_case_2 = filter_integers(test_case_2)
assert result_test_case_2 == [1, 2, 3], "Test case 2 failed"

# Test case 3: Filter integers from empty list
test_case_3 = []
result_test_case_3 = filter_integers(test_case_3)
assert result_test_case_3 == [], "Test case 3 failed"
```
This Python script defines a function `filter_integers` that filters out any non-integer values from a given list, successfully passing all test cases. The function provides a reliable and efficient way to filter integers in Python.