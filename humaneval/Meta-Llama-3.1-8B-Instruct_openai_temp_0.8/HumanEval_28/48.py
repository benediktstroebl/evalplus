### Concatenating a List of Strings into a Single String
```python
from typing import List

def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.

    Args:
        strings (List[str]): A list of strings to be concatenated.

    Returns:
        str: A single string that is the result of concatenating all input strings.

    Examples:
        >>> concatenate([])
        ''
        >>> concatenate(['a', 'b', 'c'])
        'abc'
    """
    return ''.join(strings)

# Example usage:
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```
In this script, the `concatenate` function uses the built-in `join` method of strings to concatenate all strings in the input list. The `join` method takes an iterable of strings and returns a single string that is the concatenation of all strings in the iterable. Since the input is a list of strings, we can use `join` directly without any conversion or iteration.