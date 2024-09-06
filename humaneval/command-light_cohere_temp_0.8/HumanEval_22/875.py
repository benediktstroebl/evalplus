```python
from typing import List

def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1: True success
test_case1 = [1, 2, 3, 'abc', 0, '5', 4]
assert filter_integers(test_case1) == [1, 2, 3]

# Test case 2: False failure
test_case2 = [1, 2, 3, 'abc', float('inf')]
assert filter_integers(test_case2) == []

# Test case 3: True success
test_case3 = [1, 2, 'three', 3]
assert filter_integers(test_case3) == [1, 2, 3]

print("All tests passed!")
```