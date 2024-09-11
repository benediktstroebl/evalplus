```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: The list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
print(filter_by_prefix(['hello', 'world', 'python', 'programming'], 'pro'))
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses a list comprehension to create a new list that includes only the strings from the input list that start with the given prefix. The function also includes docstrings to provide documentation and examples of usage. Finally, the script includes some test cases to demonstrate how the function works.