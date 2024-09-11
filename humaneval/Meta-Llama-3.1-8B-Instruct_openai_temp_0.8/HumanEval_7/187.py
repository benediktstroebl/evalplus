```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of strings to filter
        substring (str): Substring to search for

    Returns:
        List[str]: List of strings containing the given substring

    Example:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Test the function
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello world', 'python', 'programming'], 'world'))  # Expected output: ['hello world']
```

This script defines the `filter_by_substring` function, which takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. It uses a list comprehension to achieve this. The example use cases are demonstrated at the end of the script.