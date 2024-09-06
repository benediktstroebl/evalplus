```python
from typing import List
def concatenate(strings: List[str]):
    """ Concatenate list of strings into a single string
    :param strings: list of strings
    :return: string
    """
    return ''.join(strings)
```
This code defines a function `concatenate` which takes a list of strings as an argument and returns the concatenated string. It uses the first string (`'`).join() function to concatenate the strings in the list.

Here's a sample test:
```python
import pytest

strings = ['a', 'b', 'c']
result = concatenate(strings)

assert result == 'abc'
```

Note that this code can be used to solve the problem of concatenating a list of strings into a single string.