```python
from typing import List

def filter_integers(values):
    """ Filter given list for integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases
values_test = [1, 2, 3, 'abc', three, (four)]
result_test = filter_integers(values_test)
assert [x for x in result_test if isinstance(x, int)], "Result is not an integer list"
```