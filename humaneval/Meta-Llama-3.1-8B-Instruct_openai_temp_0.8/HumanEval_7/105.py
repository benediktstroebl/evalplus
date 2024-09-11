```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): List of strings to be filtered
    substring (str): The substring to search for in each string

    Returns:
    List[str]: List of strings that contain the given substring

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
print(filter_by_substring(['hello', 'world', 'python', 'coding'], 'o'))
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list `strings` and return only the strings that contain the given `substring`. The function is then tested with some example inputs.