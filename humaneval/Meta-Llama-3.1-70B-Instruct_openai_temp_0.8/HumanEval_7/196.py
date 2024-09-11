```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to filter.
    substring (str): A substring to filter by.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example use cases:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses a list comprehension to create a new list containing only the strings from the input list that contain the given substring. The function includes a docstring that describes its behavior, arguments, and return value, and includes example use cases to demonstrate how to use the function.