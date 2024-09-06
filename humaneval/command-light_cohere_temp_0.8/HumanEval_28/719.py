Here's a Python script with a self-contained function that concatenates strings in a list into a single string:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    :param strings: list of strings to concatenate
    :return: concatenated string
    """
    return ''.join(strings)
```
This script defines a function 'concatenate' that takes a list of strings as input and returns the concatenated string. The function uses the string ''.join(strings) to concatenate the list elements into a single string. The function is self-contained, and its purpose is to concatenate strings from a list into a single string.

Note: This solution uses Python's built-in function 'join' to concatenate strings from a list.