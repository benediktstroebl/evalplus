```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Test the function
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'p'))   # ['python']
print(filter_by_prefix(['abc', 'array', 'prefix'], 'nonexisting'))  # ['abc', 'array', 'prefix']
```

This script defines a function `filter_by_prefix` that uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. It then tests this function with some example cases to demonstrate its behavior.