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
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This script defines the `filter_by_prefix` function, which uses a list comprehension to create a new list containing only the strings from the input list that start with the given prefix. The `startswith` method is used to check if a string starts with a given prefix. The function also includes a docstring that describes its purpose, arguments, and return value. The example usage demonstrates how to use the function.