```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Given substring to filter by

    Returns:
        List[str]: Filtered list of strings containing the given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'adm']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(f"Strings containing '{substring}': {filtered_strings}")
```

This script defines the `filter_by_substring` function as requested. The function uses a list comprehension to iterate over the input list of strings and include only those that contain the given substring. The function then returns this filtered list.

The example usage at the end demonstrates how to use this function with a list of strings and a substring. The result is printed to the console.