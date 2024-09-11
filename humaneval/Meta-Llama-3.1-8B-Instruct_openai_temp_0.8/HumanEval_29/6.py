```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): A list of strings to be filtered.
    prefix (str): The prefix to look for in the strings.

    Returns:
    List[str]: A list of strings that start with the given prefix.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that uses list comprehension to filter the input list of strings based on whether they start with a given prefix. The function takes advantage of the built-in `startswith` method of strings in Python, which returns `True` if the string starts with the given prefix and `False` otherwise. The `startswith` method is used in conjunction with a list comprehension to create a new list that includes only the strings that start with the given prefix.