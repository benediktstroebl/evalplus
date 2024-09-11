```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): Input list of strings.
        prefix (str): Prefix to filter the list by.

    Returns:
        List[str]: Filtered list of strings.

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
print(filter_by_prefix(['hello', 'world', 'python', 'programming'], 'p'))  # Expected output: ['python', 'programming']
```

In this script, we use a list comprehension to create a new list that includes only the strings from the input list that start with the given prefix. The `startswith` method of the string class is used to check if a string starts with a certain prefix. If the prefix is an empty string, it matches all strings.