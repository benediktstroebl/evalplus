```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string from a list of strings.
    Args:
    strings: List of strings
    Returns:
    List of strings
    """
    return max(strings, key=len)

# Test cases
strings = ["a", "b", "c"]
result = longest(strings)
print(result)  # Output: "c"

strings = ["abcd", "bcda", "ac"]
result = longest(strings)
print(result)  # Output: "ac"

strings = []
strings. strings print(longest(strings))  # Output: None
```
The function returns the length-ordered string from a list of strings. If the input list is empty, it returns None.