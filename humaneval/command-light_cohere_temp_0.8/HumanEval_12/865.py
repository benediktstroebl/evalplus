```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list of strings.
    Args:
        strings (list): list of strings
    Returns:
    str: longest string in the list
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ["a", "b", "c"]
print("Longest:", longest(strings))  # Output: c
strings = ["a", "bb", "ccc"]
print("Longest:", longest(strings))  # Output: c
strings = []
strings = ["a"] * 10
print("Longest:", longest(strings))  # Output: a
```