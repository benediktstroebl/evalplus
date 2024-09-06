```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list of values
test_values = ['a', 3.14, 5]
result = filter_integers(test_values)
assert len(result) == 3, "Error: Filter did not work."

# Test case 2: Filter integers from a list of mixed data
test_mixed = [1, 2, 3, 'abc', {}, []]
result_mixed = filter_integers(test_mixed)
assert len(result_mixed) == 4, "Error: Filter did not work correctly for mixed data."

# Test case 3: Filter integers from an empty list
test_empty = []
result_empty = filter_integers(test_empty)
assert len(result_empty) == 0, "Error: Filter returned values from an empty list."

print("All tests passed!")
```