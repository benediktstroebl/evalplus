```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to filter.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: A list of strings that start with the given prefix.

    Example:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python', 'programming'], 'p'))  # Output: ['python', 'programming']
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. The function uses a list comprehension to create a new list that includes only the strings from the input list that start with the given prefix. The script also includes some test cases to demonstrate the function's behavior.