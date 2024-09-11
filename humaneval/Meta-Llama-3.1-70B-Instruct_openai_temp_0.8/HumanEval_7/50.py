```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): Input list of strings.
    substring (str): Substring to filter by.

    Returns:
    List[str]: Filtered list of strings.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

In this script, a list comprehension is used to filter the input list. It iterates over each string in the input list and checks if the substring is present. If the substring is present, the string is included in the output list. If not, it is skipped. The function returns the filtered list of strings.