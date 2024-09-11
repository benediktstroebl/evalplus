```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix that the strings must start with.

    Returns:
    List[str]: The filtered list of strings.
    """
    # Use a list comprehension to filter the strings list for strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]

# Test cases
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the given prefix. The function uses a list comprehension to achieve this. The script also includes two test cases to verify that the function works correctly.