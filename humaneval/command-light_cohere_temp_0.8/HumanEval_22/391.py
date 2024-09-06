```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers."""
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list of values.
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert [x for x in result_test1 if x != float('inf')] == [5], "Values are not integers."

# Test case 2: Filter integers from a list of mixed values
values_test2 = [1, 2, 3, 'abc', {}, []]
result_test2 = filter_integers(values_test2)
assert [x for x in result_test2 if x != float('inf')] == [1, 2, 3], "Values are not integers."

print("Test cases passed!")
```