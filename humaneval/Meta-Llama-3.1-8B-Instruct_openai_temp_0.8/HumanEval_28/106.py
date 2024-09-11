### Concatenating List of Strings in Python
#### Using `join()` Method

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): List of strings to concatenate.

    Returns:
        str: Concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    if not strings:
        return ''
    return ''.join(strings)

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['Hello','', 'World!']))  # 'Hello World!'
```

In this script, we use the `join()` method to concatenate the strings in the list. The `join()` method requires all the strings to be concatenated to be in a single iterable (in this case, a list). If the input list is empty, an empty string is returned.