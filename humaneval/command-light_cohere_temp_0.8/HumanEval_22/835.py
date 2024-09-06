```python
from typing import List

def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test the function with various inputs
values_test = [['a', 3.14, 5, (1, 2, 3, 'abc', [], {})]
assert filter_integers(values_test) == [5, 3, 1, 2, 3]

# Test with various types of values
values_dynamic = [1, 2, 'abc', (5, 6), []]
assert filter_integers(values_dynamic) == [1, 2, 'abc']
```