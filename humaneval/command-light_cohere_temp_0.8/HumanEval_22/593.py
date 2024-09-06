```python
from typing import List

def filter_integers(values:
    """ Filter given list of any python values only for integers"""
    return [x for x in values if isinstance(x, int)]

# Test cases
test_values = [['a', 3.14, 5], [1, 2, 'abc', {}], [(), []]

test_results = []

for values in test_values:
    test_results.add(filter_integers(values))

assert len(test_results) == 4
assert all(test_results == [5, 1, 2, 3])

print("All tests passed!")
```