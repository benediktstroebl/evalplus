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
The function concatenates a list of strings into a single string using the 'join' method. The function is designed to work correctly with any list of strings, and the tests pass the output correctly.