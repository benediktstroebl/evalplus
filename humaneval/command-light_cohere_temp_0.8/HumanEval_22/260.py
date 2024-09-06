```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1: Filter integers from a list
values_test1 = ['a', 3.14, 5]
result_test1 = filter_integers(values_test1)
assert len(result_test1) == 2

# Test case 2: Filter integers from a tuple
values_test2 = (1, 2, 3, 'abc', {}, [])
result_test2 = filter_integers(values_test2)
assert len(result_test2) == 4

# Test case 3: Filter integers from an list of any data type
values_test3 = [1, 2, 3, 'abc', (), [])
result_test3 = filter_integers(values_test3)
assert len(result_test3) == 3
```