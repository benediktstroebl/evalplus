```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
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
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
print(filter_by_prefix(['hello', 'world', 'python'], 'p'))
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses a list comprehension to create a new list that only includes strings that start with the given prefix. The function is then tested with some example inputs.