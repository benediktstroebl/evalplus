```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.
    Parameters:
    strings: List of strings
    substring: The substring to filter for.
    Returns: filtered list of strings that contain the given substring.
    """

    test cases:
    >>> test_strings = ['abc', 'bacd', 'cde', 'array', 'aabb']
    >>> test_substring = 'a'
    >>> filter_by_substring(test_strings, test_substring)
    ['abc', 'array']
    """
    return [string for string in strings if string.find(substring) != -end]
```
This function uses the .find() method to check if each string in the input list contains the given substring.