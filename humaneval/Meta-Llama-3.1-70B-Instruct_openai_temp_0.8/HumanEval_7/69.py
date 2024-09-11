```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring to filter by.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script uses a list comprehension to create a new list that only includes the strings from the input list that contain the given substring. The `in` operator is used to check for the presence of the substring in each string. The function is well-documented with a docstring that explains its purpose, parameters, and return value.