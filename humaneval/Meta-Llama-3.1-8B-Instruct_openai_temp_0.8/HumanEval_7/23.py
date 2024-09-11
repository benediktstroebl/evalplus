```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings to be filtered.
        substring (str): The substring that the strings must contain.

    Returns:
        List[str]: The filtered list of strings.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world'], 'ld'))  # Output: ['world']
```

This script defines a function `filter_by_substring` that filters a list of strings and returns a new list with only the strings that contain the specified substring. The function uses a list comprehension to efficiently create the filtered list. The test cases at the end demonstrate the function's behavior with different inputs.