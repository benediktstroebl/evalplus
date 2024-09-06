```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with different input values
test_values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, []]
assert filter_integers(test_values) == [5, 3, 1, 2]
```