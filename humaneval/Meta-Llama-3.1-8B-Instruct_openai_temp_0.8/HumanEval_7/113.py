```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings
    substring (str): The substring to search for

    Returns:
    List[str]: Filtered list of strings

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage:
strings_to_filter = ['abc', 'bacd', 'cde', 'array']
substring_to_search = 'a'
filtered_strings = filter_by_substring(strings_to_filter, substring_to_search)
print(filtered_strings)  # Output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function which uses list comprehension to filter the input list of strings. It returns a new list that includes only the strings that contain the specified substring. The example usage at the end demonstrates how to use this function.