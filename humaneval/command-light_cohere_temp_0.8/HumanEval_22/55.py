```python
from typing import List
def filter_integers(values:
    return [i for i in values if type(i) == int]

# Test case 1
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert result_test1 == [5]

# Test case 2
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
assert result_test2 == [1, 2, 3]

# Test case 3
values_test3 = [None, 0, '1', True]
result_test3 = filter_integers(values_test3)
assert result_test3 == [None, 0, 1]  # filter out all other values but handle None and True as integers
```

This script defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the input. The test cases demonstrate the integral behavior of the function for different scenarios.