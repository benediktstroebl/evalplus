```python
from typing import List
def filter_integers(values):
    """ Filter given list for integers."""
    return [i for i in values if isinstance(i, int)]

# Test the function with known good inputs
print(filter_integers(['a', 3.14, 5]))  # ['5]
print(filter_integers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
print(filter_integers([10, 20, 'hello'])))    # []
```