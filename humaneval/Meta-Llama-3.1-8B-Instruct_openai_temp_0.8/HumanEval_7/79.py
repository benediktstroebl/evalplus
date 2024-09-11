```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring to search for in each string.

    Returns:
    List[str]: A list of strings that contain the given substring.

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world'], 'l'))  # Output: ['hello', 'world']
print(filter_by_substring([], 'x'))  # Output: []
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. It uses a list comprehension to achieve this in a concise and efficient way. The example usage at the end demonstrates how to use this function with different inputs.