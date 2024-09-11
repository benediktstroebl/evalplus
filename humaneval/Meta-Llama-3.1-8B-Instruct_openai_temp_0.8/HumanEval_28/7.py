```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string

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

# Example usage:
print(concatenate(['Hello, ', 'world!']))
print(concatenate([]))
print(concatenate(['a', 'b', 'c']))
```

In this script, the `concatenate` function uses Python's built-in `join` method to concatenate the strings in the `strings` list. The `join` method takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings. If the string it's called on is empty (as in this case with `''`), it simply concatenates the strings without anything in between.