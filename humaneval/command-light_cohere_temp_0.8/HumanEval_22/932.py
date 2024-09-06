```python
from typing import List
def filter_integers(values:
    return [i for i in values if isinstance(i, int)]

# Test case 1: Basic integer filter
values = ['a', 3.14, 5]
result = filter_integers(values)
assert len(result) == 3, "Error: Expected list of integers, got {}"

# Test case 2: Empty list
values = []
result2 = filter_integers(values)
assert len(result2) == 0, "Error: Expected empty list, got {}"

# Test case 3: Non-integer elements
values = [1, 2, 3, 'abc', {}, []]
result3 = filter_integers(values)
assert len(result3) == 4, "Error: Expected list with integer elements, got {}"

print("All tests passed!")
```