```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): List of input strings
        substring (str): The substring to search for in each string

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
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on whether they contain a given substring. The function uses a list comprehension to create a new list containing only the strings that have the substring. The script includes docstrings and example use cases to demonstrate how to use the function.