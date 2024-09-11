### Filtering Strings by Prefix
#### A Python Script
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): A list of strings to be filtered.
    - prefix (str): The prefix to filter the strings by.

    Returns:
    - List[str]: A list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered = filter_by_prefix(strings, prefix)
print(filtered)  # Output: ['abc', 'array']
```

In this script, we use a list comprehension to create a new list that includes only the strings that start with the given prefix. The `startswith()` method of Python's string type is used to check if a string starts with a given prefix.