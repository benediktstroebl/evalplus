```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example use cases:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that filters a list of strings based on the presence of a given substring. It uses list comprehension to create a new list containing only the strings that include the substring. The function is documented with a docstring, and example use cases are provided to demonstrate its usage.