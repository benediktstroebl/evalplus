### Concatenating a List of Strings into a Single String

We will use the `join()` method to concatenate a list of strings. This method is more memory efficient than using the `+` operator because it avoids creating intermediate strings.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

    Args:
        strings (List[str]): A list of strings to be concatenated

    Returns:
        str: A single string after concatenating all input strings

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)
```

You can use this function as follows:

```python
# Test the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```