```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings
    substring (str): The substring to search for in the input strings

    Returns:
    List[str]: A list of strings that contain the given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'xyz']
substring = 'a'
filtered = filter_by_substring(strings, substring)
print(f"Filtered strings containing '{substring}': {filtered}")
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The example usage demonstrates how to use the function with a list of strings and a substring, and prints the resulting filtered list.