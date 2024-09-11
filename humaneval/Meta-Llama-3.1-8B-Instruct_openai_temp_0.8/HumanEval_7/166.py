```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings
    substring (str): The substring to filter by

    Returns:
    List[str]: Filtered list of strings
    """
    # Use a list comprehension to filter the input list
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['apple', 'banana', 'cherry'], 'an'))  # ['banana']
print(filter_by_substring(['hello', 'world'], 'abc'))  # []
```

This script uses a list comprehension to filter the input list `strings` only for strings that contain the given `substring`. The `if` condition inside the list comprehension checks for the presence of the substring in each string. The resulting filtered list is then returned by the function.

The example usage at the end demonstrates how to use the `filter_by_substring` function with different input lists and substrings.