```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter the list by.

    Returns:
        List[str]: The filtered list of strings.

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Test cases
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
print(filter_by_prefix(['python', 'java', 'javascript', 'kotlin'], 'j'))  # Expected output: ['java', 'javascript']
```

This script uses a list comprehension to filter the input list `strings` and return only the strings that start with the given `prefix`. The `startswith` method is used to check if a string starts with a given prefix. The test cases are included at the end to demonstrate the function's usage.