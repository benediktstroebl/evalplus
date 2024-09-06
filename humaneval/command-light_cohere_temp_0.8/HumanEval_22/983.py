```python
from typing import List

def filter_integers(values):
    """ Filter given list of any python values only for integers."""
    return [num for num in values if isinstance(num, int)]

# Test cases
test_filter = []
test_filter.add([1, 2, 3, 'abc', [5])
test_filter.add([6])
test_filter.add([7])
test_filter.add([8])
test_filter.add([8])
test_filter.add([1.14])
test_filter = test_filter.verify_integers(test_filter)

# Test result: [1, 2, 3, 5, 6]
```