```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): A list of strings to be filtered.
    - prefix (str): The prefix to filter by.

    Returns:
    - List[str]: A list of strings that start with the given prefix.

    Example:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Testing the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'py'))  # Output: ['python']
print(filter_by_prefix(['happy', 'birthday', 'to', 'you'], 'b'))  # Output: ['birthday', 'to', 'you']
```

This Python script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses a list comprehension to iterate over the input list and includes strings that start with the given prefix. The function is then tested with several examples to demonstrate its usage.