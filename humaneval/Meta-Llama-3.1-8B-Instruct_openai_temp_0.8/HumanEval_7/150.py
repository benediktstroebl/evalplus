```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring that strings should contain.

    Returns:
    List[str]: A list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Should print: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Should print: ['abc', 'bacd', 'array']
```

In this script, a list comprehension is used to filter the input list `strings` for strings that contain the given `substring`. The `if substring in string` condition is used to check if each string contains the substring. The filtered list of strings is then returned. The examples provided in the docstring are demonstrated at the end of the script.