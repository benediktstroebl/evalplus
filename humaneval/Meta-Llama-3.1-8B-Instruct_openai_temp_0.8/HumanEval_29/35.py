### Filter by Prefix Function
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
This script defines a function `filter_by_prefix` that uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method of Python strings is used to check if a string starts with a given prefix.

The script also includes an example usage of the function, which demonstrates how to call the function with a list of strings and a prefix, and prints the result.