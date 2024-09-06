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
This code provides a self-contained function `concat()` that takes a list of strings as an argument and returns the concatenated string. 

It uses a type hint `List[str]` to let the function work only with strings and uses the `join()` method to create the concatenated string.