```python
from typing import List
def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test the function with markdown test data
values_test = [1, 2, 3, 'abc', {}, [5], [3.14]]
filtered = filter_integers(values_test)
assert filtered == [1, 2, 3, 5]
```