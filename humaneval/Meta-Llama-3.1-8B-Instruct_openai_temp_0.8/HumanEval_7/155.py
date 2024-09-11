Here's a self-contained Python script that solves the problem:

```python
"""
This module provides a function to filter a list of strings based on a given substring.
"""

from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    - strings (List[str]): Input list of strings to be filtered
    - substring (str): Substring to search in the input list of strings

    Returns:
    - List[str]: Filtered list of strings containing the given substring

    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function that uses a list comprehension to filter the input list of strings based on the given substring. The function then is tested with the provided examples at the end of the script.