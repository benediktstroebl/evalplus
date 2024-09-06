Here's the solution:
```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    Args:
    strings: list of strings to concatenate
    Returns:
    concatenated string
    """
    return ''.join(strings)
```
This function takes a list of strings as an argument and concatenates them into a single string using the `join` method. The type hint in the string is used to let the user of the function know that the expected argument should be a list of strings.

The code is well-formatted and follows the PEP 8 style guidelines for Python code, which makes it readable and maintainable.