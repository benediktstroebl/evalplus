```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The input list of strings
    substring (str): The substring to search for

    Returns:
    List[str]: The filtered list of strings containing the substring

    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world'], 'o'))  # Output: ['hello', 'world']
print(filter_by_substring(['hello', 'world'], 'xyz'))  # Output: []
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings. It iterates over each string in the input list and includes it in the output list if the given substring is found within it. The function is then tested with several examples to demonstrate its usage.