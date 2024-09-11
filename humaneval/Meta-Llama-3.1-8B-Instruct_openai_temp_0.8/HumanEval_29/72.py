```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings to be filtered.
    prefix (str): The prefix that strings should start with to be included in the output.

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
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
print(filter_by_prefix(['hello', 'world', 'python'], 'w'))
```

This script defines the `filter_by_prefix` function that filters a list of strings based on a given prefix, using a list comprehension to achieve this efficiently. The function is then tested with a few examples to demonstrate its usage.