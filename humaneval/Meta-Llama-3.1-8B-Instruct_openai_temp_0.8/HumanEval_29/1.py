```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter the strings with.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    # Use a list comprehension to create a new list that includes only the strings that start with the prefix
    return [s for s in strings if s.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```

This script defines the `filter_by_prefix` function as specified, and includes a docstring that explains how to use the function and provides example usage. The function uses a list comprehension to create a new list that includes only the strings from the input list that start with the specified prefix. The script also includes two test cases to demonstrate how the function works.