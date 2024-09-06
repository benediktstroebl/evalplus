```python
from typing import List

def filter_integers(values: List[Any]):
    """ Filter given list for integers"""
    return [x for x in values if isinstance(x, int)]

# Testing the function
test_values = [1, 2, 3, 'abc', 4, 'c']
test_output = filter_integers(test_values)
assert len(test_output) == 6, "Testing failed"

test_empty = []
test_output2 = filter_integers(test_empty)
assert len(test_output2) == 0, "Testing failed"

test_large = [123123123, 456, 678901234]
test_output3 = filter_integers(test_large)
assert len(test_output3) == 3, "Testing failed"
```