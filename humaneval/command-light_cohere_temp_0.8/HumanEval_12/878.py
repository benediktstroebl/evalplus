```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    return max(strings, key=len)

# Unit tests
strings = ["a", "bb", "ab", "aaa", "xx"]
longest_result = longest(strings)
print("Longest:", longest_result) # Output: "aaa"

strings = ["a", "bb", "cc"]
longest_result = longest(strings)
print("Longest:", longest_result) # Output: "bb"

strings = List()
longest_result = longest(strings)
print("Longest:", longest_result) # Output: None
```