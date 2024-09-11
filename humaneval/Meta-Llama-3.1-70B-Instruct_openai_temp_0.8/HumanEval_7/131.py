```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The list of strings to filter.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A new list containing only the strings that include the substring.
    """
    return [string for string in strings if substring in string]

# Example use cases:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function as specified. It uses a list comprehension to create a new list containing only the strings from the input list that include the given substring. The function includes type hints and a docstring for clarity. Example use cases are also provided to demonstrate the function's behavior.