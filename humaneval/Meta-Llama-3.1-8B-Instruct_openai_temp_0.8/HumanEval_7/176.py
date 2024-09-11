```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered
    substring (str): The substring to search for in each string

    Returns:
    List[str]: A list of strings that contain the given substring

    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    # Use list comprehension to iterate over each string in the input list
    # and include it in the output list if it contains the substring
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses list comprehension to create a new list containing only the strings from the input list that contain the given substring. The function includes docstrings to explain its purpose, arguments, return value, and provide an example usage.