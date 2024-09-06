```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string in the list.
    """
    list must be of strings, not empty
    if not strings:
        return None
    max_len = 0
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
    return max_len
test_longest = [
    "a", "bb", "abc",
    "bc", "abc"
]
result = longest(test_longest)
assert result == 3
```