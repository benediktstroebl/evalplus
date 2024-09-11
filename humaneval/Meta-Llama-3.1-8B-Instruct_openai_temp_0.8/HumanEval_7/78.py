```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A new list containing only the strings that contain the substring.
    """
    return [string for string in strings if substring.lower() in string.lower()]

# Example use cases
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a string to filter by. It uses list comprehension to create a new list containing only the strings that contain the substring. The comparison is case-insensitive by converting both the substring and the strings to lowercase.