```python
# The following code is copied directly from the markdown code block above this comment.

from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ""
    for string in strings:
        result += string
    return result
``` 

This code defines a function called `concatenate` that takes a list of strings as input and returns a single string that concatenates all the strings in the list separated by spaces. The function is tested twice, first with an empty list then a list of three letters, which it passes.