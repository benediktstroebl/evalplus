```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): A substring that must be present in the strings.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

In this script, we're using a list comprehension to filter the input list of strings. The `if substring in string` condition checks if the substring is present in each string, and only includes the string in the output list if it is. The function returns the filtered list of strings.