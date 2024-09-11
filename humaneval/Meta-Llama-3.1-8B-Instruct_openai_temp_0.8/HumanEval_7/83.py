```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    - strings (List[str]): The list of strings to be filtered.
    - substring (str): The substring to be searched in the strings.

    Returns:
    - List[str]: A list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['hello', 'world'], 'o'))
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. The function uses a list comprehension to achieve this. The example use cases are included in the docstring and are executed at the end of the script.