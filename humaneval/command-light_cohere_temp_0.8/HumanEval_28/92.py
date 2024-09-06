```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatented string
    """
    return ''.join(strings)

# Test cases
strings = ["hello", "world"]
result = concatenate(strings)
assert result == "hello world"

strings = []
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

strings = ["hello", "world"]
strings = ["a", "world"]
result = concatenate(strings)
assert result == "a world"
```
This script defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It uses the simple list comprehension to combine the strings into a single string.