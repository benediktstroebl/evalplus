### Concatenating List of Strings into a Single String
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
```

### Explanation
The `concatenate` function uses the `join` method to concatenate all strings in the input list into a single string. The `join` method returns a string in which the elements of the input list have been joined together using the string on which the `join` method was called. Since we want to concatenate the strings without any separator, we use an empty string (`''`) as the argument to `join`.