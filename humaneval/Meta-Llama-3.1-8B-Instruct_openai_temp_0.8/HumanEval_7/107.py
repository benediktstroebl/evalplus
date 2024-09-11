```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings to be filtered
        substring (str): Substring to search for in the input strings

    Returns:
        List[str]: Filtered list of strings containing the given substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the given substring. The function uses a list comprehension to achieve this. The script also includes docstrings and example use cases to demonstrate the function's behavior.