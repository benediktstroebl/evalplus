```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: The filtered list of strings.
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'py'))  # ['python']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. It uses a list comprehension to achieve this, which is a concise and efficient way to create a new list by iterating over the input list. The `startswith` method of the string class is used to check if a string starts with the given prefix.