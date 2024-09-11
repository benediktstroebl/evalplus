```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string that is the result of concatenating all strings in the input list.

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```

However, the built-in `str.join()` method already does this for us, so we can simplify it to:

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
    strings (List[str]): A list of strings to be concatenated.

    Returns:
    str: A single string that is the result of concatenating all strings in the input list.

    Examples:
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)
```

This code simply joins all the strings in the input list together without any separator, effectively concatenating them into a single string.