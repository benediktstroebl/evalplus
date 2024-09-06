```python
from typing import List

def filter_integers(values:
    """ Returns list of integers only"""
    return [x for x in values if isinstance(x, int)]

# Test cases 

test_values = [["a", 3.14, 5, 1, 2, 3, 'abc', {}, [0]]

expected = [5]

test_results = filter_integers(test_values)

assert expected == test_results
```