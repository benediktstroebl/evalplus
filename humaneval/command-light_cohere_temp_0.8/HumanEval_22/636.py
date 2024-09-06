```python
from typing import List

def filter_integers(values:
    """
    filtered = [x for x in values if isinstance(x, int)]
    return filtered

# Test case 1
test_case1 = [1, 2, 3, 'abc', 4, 5]
assert filter_integers(test_case1) == [1, 2, 3]

# Test case 2
test_case2 = [1, 2, 3, {}]
assert filter_integers(test_case2) == [1, 2, 3]

# Test case 3
test_case3 = ['a', 3.14, 5]
assert filter_integers(test_case3) == [3.14, 5]
```