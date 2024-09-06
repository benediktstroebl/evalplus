```python
from typing import List

def filter_integers(values):
    """ Filter given list for only integers."""
    return [x for x in values if isinstance(x, int)]

# Test the function with markdown code block values
test_filter_integers = [['a', 3.14, 5], [1, 2, 3, 'abc', {}, []]
result = filter_integers(test_filter_integers)
assert result == [5, 1, 2, 3]
```