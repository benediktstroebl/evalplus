```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring that should be present in the strings.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to create a new list with strings that contain the substring
    return [s for s in strings if substring in s]

# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script uses list comprehension to create a new list with strings that contain the given substring. The built-in `in` operator checks if a string contains a substring. If the substring is present in a string, the string is included in the new list. If not, it's skipped. This results in a filtered list that only includes strings with the specified substring.