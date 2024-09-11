```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The input list of strings.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A new list containing only the strings that contain the substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```