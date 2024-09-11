### Concatenate List of Strings into a Single String

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): List of strings to be concatenated.

    Returns:
        str: Concatenated string.

    Example:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    # Use the join() method to concatenate all strings in the list
    # into a single string, with no separator
    return ''.join(strings)
```

This script defines a function `concatenate()` that takes a list of strings as input and returns a single concatenated string. The function uses the `join()` method to concatenate all strings in the list, resulting in a single string. The `join()` method takes an iterable (in this case, the list of strings) and concatenates its elements into a single string, with the string passed as the first argument (in this case, an empty string) as the separator.