```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Test the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['test1', 'test2', 'test3'], 'tes'))  # Output: ['test1', 'test2', 'test3']
```

This script defines and tests the `filter_by_prefix` function, which uses a list comprehension to filter the input list of strings based on the provided prefix. The function returns a new list containing only the strings that start with the given prefix. If no strings match the prefix, an empty list is returned. The script includes docstrings and example use cases for clarity and documentation.