```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The list of strings to filter.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A new list containing only the strings that contain the substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    # Use list comprehension to create a new list with only the strings that contain the substring
    return [string for string in strings if substring in string]


# Test the function
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function as specified and includes a docstring that explains the purpose of the function, its parameters, its return value, and provides some example use cases. It then tests the function with the provided examples to ensure it works as expected.