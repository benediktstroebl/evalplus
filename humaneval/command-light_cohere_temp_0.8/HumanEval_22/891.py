```python
from typing import List
def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1
test_values = ['a', 3.14, 5]
assert filter_integers(test_values) == [5]

# Test case 2
test_data = [1, 2, 3, 'abc', {}, []]
assert filter_integers(test_data) == [1, 2, 3]
```