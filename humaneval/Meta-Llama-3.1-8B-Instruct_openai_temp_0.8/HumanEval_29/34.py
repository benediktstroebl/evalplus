```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings to filter.
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


# Test cases
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['apple', 'banana', 'cherry'], 'b'))  # Output: ['banana']
print(filter_by_prefix(['hello', 'world'], 'foo'))  # Output: []
```

This script defines the `filter_by_prefix` function, which uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The function then returns the filtered list of strings. The script includes several test cases to demonstrate the function's behavior.