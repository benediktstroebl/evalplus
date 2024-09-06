```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings (List[str]): List of strings to concatenate
    Returns:
        str: Concatenentated string
    """
    return ''.join(strings)
```

This script defines a function `concatenate` which takes a list of strings as input and returns the concatenated string. The function uses the important `List[str]` type hint to indicate that the input is a list of strings, and it uses the `join` method to concatenate the strings into a single string and returns the result.