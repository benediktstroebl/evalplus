```python
from typing import List

def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list of any values
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert result_test1 == [5], "Invalid filtering of non-integer elements"

# Test case 2: Filter integers from a list of numbers
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
assert result_test2 == [1, 2, 3], "Invalid filtering of non-integer elements"

# Test case 3: Filter integers from a list of strings
values_test3 = ['a', 3, 'bc', '123']
result_test3 = filter_integers(values_test3)
assert result_test3 == [3,], "Invalid filtering of non-integer elements"
```
The provided code defines a function **filter_integers** that takes a list of values and returns a new list containing only the integers from the original list. The code is then used to test the function with three different cases, and passes all tests successfully.