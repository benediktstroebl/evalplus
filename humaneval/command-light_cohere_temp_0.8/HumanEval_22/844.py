```python
from typing import List

def filter_integers(values):
    return [x for x in values if isinstance(x, int)]

# Test case 1: Filter integers from a list of values
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 2, "Failed in test case 1"

# Test case 2: Filter integers from a list of mixed data types
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 4, "Failed in test case 2"

# Test case 3: Filter integers from empty list
values3 = []
result3 = filter_integers(values3)
assert len(result3) == 0, "Failed in test case 3"

print("All tests passed!")
```