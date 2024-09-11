```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix that the strings should start with.

    Returns:
        List[str]: The filtered list of strings.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(filtered_strings)  # Output: ['abc', 'array']
```

This script uses a list comprehension to filter the input list of strings. The `startswith` method of a string is used to check if the string starts with the given prefix. The filtered list of strings is then returned.