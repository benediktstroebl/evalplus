```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to filter.
    prefix (str): The prefix to filter by.

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

This script defines a function `filter_by_prefix` that uses list comprehension to filter a list of strings for ones that start with a given prefix. The `startswith` method is used to check if a string starts with the given prefix. The script also includes example usage and a test case to demonstrate the function's behavior.