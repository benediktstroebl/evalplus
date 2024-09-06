```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function with known good inputs and known bad inputs
values_good = [5, 3, 'three', (])
values_bad = [1, 2, 'abc', {}, [{}]]

assert filter_integers(values_good) == [5, 3, 'three']
assert filter_integers(values_bad) == []

# These will fail, test them please
values_fail = [1, 2, 'not_an_integer']

print("Failed test:", filter_integers(values_fail))
```