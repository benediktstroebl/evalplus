```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test cases
test_filter_integers = [
    ['a', 3.14, 5], [1, 2, 3, 'abc', {}, []],
    [10, 20, 30], ['foo', 'bar', 'baz']
]

all(filter_integers(test) for test in test_filter_integers)  # True
```