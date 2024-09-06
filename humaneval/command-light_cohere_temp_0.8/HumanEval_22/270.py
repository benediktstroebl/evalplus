```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values for integers."""
    return [i for i in values if isinstance(i, int)]

# Test cases
test_values = [1, 2, 3, 'abc', {}, [1, 2, 3, 4]]
test_output = filter_integers(test_values)
assert test_output == [1, 2, 3]

test_str_values = ['a', 3.14, 5]
test_output = filter_integers(test_str_values)
assert test_output == [5]
```
This script defines a function **filter_integers** that filters a given list of values, returning a new list containing only the integers. The function uses a list comprehension to filter out the integers from the input list. The test cases demonstrate the values of the input and the expected output of the **filter_integers** function.