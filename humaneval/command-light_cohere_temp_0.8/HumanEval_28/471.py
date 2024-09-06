```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
        strings: list of string
    Returns:
        str: concatenated string
    """
    return ''.join(strings)
```
This code defines a function called **concatenate** that takes a list of strings as input and returns the concatenated string. 

The function uses the **join** method to concatenate the strings, which is a built-in method in Python that returns a new string formed by joining the elements of an iterable.