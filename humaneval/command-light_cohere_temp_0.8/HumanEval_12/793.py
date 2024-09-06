```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the length of the longest string.
    :type strings: List[str]
    """
    return max(len(str), key=len)

# Test case 1
test_case1 = ["a", "b", "c"]
assert longest(test_case1) == 3

# Test case 2
test_case2 = ["a", "bb", "ccc"]
assert longest(test_case2) == 3

# Test case 3
test_case3 = []
assert longest(test_case3) is None

# Test case 4
test_case4 = ["a", "bb", "ccc", "a"]
assert longest(test_case4) == 2
```