Here is a Python script with a self-contained function that solves the problem of concatenating list of strings into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings
    Returns:
        string
    """
    return ''.join(strings)
```
The function takes a list of strings as input and returns a string. The function uses the 'join' method to concatenate all the strings in the list into a single string. The resulting string is returned as the output of the function.