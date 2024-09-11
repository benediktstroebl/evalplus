### Filter Strings by Prefix
#### Problem Statement
Given a list of strings and a prefix, return a new list containing only the strings that start with the given prefix.

#### Solution
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A new list containing only the strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    # Use list comprehension to filter the strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses list comprehension to create a new list containing only the strings that start with the given prefix. The function returns this new list. The example usage at the end demonstrates how to use this function with a sample list of strings and prefix.