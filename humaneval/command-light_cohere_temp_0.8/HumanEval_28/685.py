```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of strings to concatenate  
    Returns:
        string
    """
    return ''.join(strings)
```
This code defines a function called `concatenate` that takes a list of strings as an argument and returns a concatenated string. The function uses the string method `join` to concatenate all the strings in the list into a single string and then returns the result.