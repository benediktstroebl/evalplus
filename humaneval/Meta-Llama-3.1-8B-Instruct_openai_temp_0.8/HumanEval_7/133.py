```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered
        substring (str): The substring to search in the strings

    Returns:
        List[str]: A list of strings that contain the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Test the function
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # Expected output: ['hello', 'world']
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter a list of strings based on whether they contain a given substring. It then tests the function with a few examples.