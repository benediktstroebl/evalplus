### String Concatenation Script
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
    return ''.join(strings)

# Test the function
if __name__ == "__main__":
    print(concatenate([]))  # Output: ''
    print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
    print(concatenate(['Hello ', 'World!']))  # Output: 'Hello World!'
```
In this script, we use the `join()` function to concatenate the list of strings. The `join()` function takes an iterable of strings and concatenates them with the string it's called on in between each pair of strings. Since we're using an empty string (`''`), it concatenates the strings without any separator.