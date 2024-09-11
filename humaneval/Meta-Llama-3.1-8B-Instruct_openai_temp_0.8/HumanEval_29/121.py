### Filter by Prefix Function
#### A Python Function to Filter a List of Strings by Prefix

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

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
print(filter_by_prefix(strings, prefix))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. It uses a list comprehension to achieve this. The function is well-documented with a docstring that includes examples of usage. The example usage at the end of the script demonstrates how to use the function.