```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): The list of strings to be filtered.
    - prefix (str): The prefix to filter by.

    Returns:
    - List[str]: A list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage
strings = ['abc', 'bcd', 'cde', 'array']
print(filter_by_prefix(strings, 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix([], 'a'))      # Output: []
print(filter_by_prefix(['test', 'test1', 'test2'], 'test'))  # Output: ['test', 'test1', 'test2']
```

In this script, we use a list comprehension to filter the input list `strings` and return a new list that only includes strings that start with the given `prefix`. The `startswith()` method of the string class is used to check if a string starts with a given prefix.