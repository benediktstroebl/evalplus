```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'p'))  # Expected output: ['python']
```

This script defines the `filter_by_prefix` function, which takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to create the new list, and the `startswith` method to check if a string starts with the prefix. The script also includes test cases to demonstrate the function's behavior.