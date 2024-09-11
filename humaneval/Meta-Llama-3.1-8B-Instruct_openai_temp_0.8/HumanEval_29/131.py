```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): The list of strings to be filtered.
    - prefix (str): The prefix to filter by.

    Returns:
    - List[str]: The filtered list of strings.

    Example:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Testing the function
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```

This script defines the `filter_by_prefix` function and includes example use cases. It uses a list comprehension to filter the input list `strings` based on whether each string starts with the given `prefix`. The `startswith` method of Python strings is used for this purpose.