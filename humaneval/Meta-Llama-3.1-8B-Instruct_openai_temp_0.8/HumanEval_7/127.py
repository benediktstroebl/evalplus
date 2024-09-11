```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Use a list comprehension to filter the list of strings
    # The expression string in substring checks if substring is a substring of string
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. It uses a list comprehension to achieve this in a concise and efficient manner. The docstring includes example usage, as specified.