```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(filtered_strings)
```

This script defines a function `filter_by_prefix` that takes two parameters: `strings` (the list of strings to be filtered) and `prefix` (the prefix to filter by). It uses a list comprehension to create a new list that includes only the strings from `strings` that start with the `prefix`. The script also includes two example usage cases as docstrings and an additional example usage at the end of the script.