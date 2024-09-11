```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Testing the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python', 'program'], 'p'))  # Output: ['python', 'program']
```

This script uses a list comprehension to create a new list that includes only the strings from `strings` that start with `prefix`. The `startswith()` method is used to check if a string starts with a given prefix. If the prefix is empty, the function returns the input list as is because an empty string is considered to start with any string.