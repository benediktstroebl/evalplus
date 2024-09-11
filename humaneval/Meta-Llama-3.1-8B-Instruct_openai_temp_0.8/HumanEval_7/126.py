```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The list of strings to filter.
    substring (str): The substring to search for.

    Returns:
    List[str]: A list of strings that contain the given substring.

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # Expected output: ['hello', 'world']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to achieve this. The test cases at the end demonstrate the function's behavior.