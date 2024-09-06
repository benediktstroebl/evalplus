```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings (List[str]): List of strings to concatenate

    Returns:
    str: Concatenated string
    """
    return ''.join(strings)
```

This code defines a function called `concatenate` that takes a list of strings as an argument and returns a concatenated string. The function uses the string method `join` to concatenate the strings.