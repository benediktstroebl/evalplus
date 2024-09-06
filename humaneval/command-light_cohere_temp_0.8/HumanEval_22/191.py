```python
from typing import List

def filter_integers(values):
    return [i for i in values if isinstance(i, int)]

# Test cases
test_filter_integers = [
    ['a', 3.14, 5], [1, 2, 3, 'abc', {}, []], [1, 2, 3]
]

assert filter_integers(test_filter_integers[0]) == [5]
assert filter_integers(test_filter_integers[1]) == [1, 2, 3]
assert filter_integers(test_filter_integers[2]) == [1, 2, 3]
```