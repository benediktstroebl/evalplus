```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    Args:
        strings (List[str]): list of strings
    Returns:
        str: longest string
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'

strings = ["hello", "world"]
print(longest(strings))  # Output: 'hello'

strings = []
strings. = some_string
strings. strings string
print(longest(strings))  # Output: 'some_string'
```

The code defines a function `longest` that takes a list of strings and returns the longest string. It then tests this function with different lists of strings and prints the result.