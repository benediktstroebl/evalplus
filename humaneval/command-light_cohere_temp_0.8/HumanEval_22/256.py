```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test the function with markdown code block values
test_values = [['a', 3.14, 5, 1, 2, 3, 'abc', {}, [], ]

assertEqual(filter_integers(test_values), [5])
assertEqual(filter_integers(test_values), [1, 2, 3])
assert len(filter_integers(test_values)) == 3)
```