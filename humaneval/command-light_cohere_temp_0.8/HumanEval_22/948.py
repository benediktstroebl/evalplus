```python
from typing import List
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test case 1: Specific integers
test_case1 = [1, 2, 3, 5]
assert filter_integers(test_case1) == [1, 2, 3]

# Test case 2: List of strings that contain only digits
test_case2 = ['123', '456', 'abc']
assert filter_integers(test_case2) == []

# Test case 3: List with one float
test_case3 = [1, 2, 3. lastly
assert filter_integers(test_case3) == [1, 2, 3]

# Test case 4: Specific floats
test_case4 = [3.14, 5]
assert filter_integers(test_case4) == [5]
```
The code defines a function called `filter_integers` that filters a list of any Python values and returns a new list containing only the integers. The test cases demonstrate the values, such as integers and strings containing only digits, are correctly filtered, while floats and non-numeric strings are ignored.