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
This code defines a function called `concat` that takes in a list of strings as an argument. It uses the common method to concatenate the strings within the list and returns the result as a string.