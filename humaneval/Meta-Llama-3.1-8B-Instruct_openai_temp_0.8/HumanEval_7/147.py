```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings
    substring (str): Substring to look for in strings

    Returns:
    List[str]: Filtered list of strings containing the given substring

    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to filter the input list and return a new list containing only the strings that contain the given substring. The function is then tested with two example use cases.