```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: The concatenated string

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
```

In this script, the `concatenate` function takes a list of strings as input and returns a single string that is the concatenation of all the input strings. The `''.join(strings)` expression is used to concatenate the strings. This works by creating a new string and adding the contents of each string in `strings` to it. If `strings` is empty, it returns an empty string.