```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with a variety of inputs
test_values = [['a', 3.14, 5], [1, 2, 'abc', [], {}]
assert filter_integers(test_values) == [5, 1, 2, 'abc']
```