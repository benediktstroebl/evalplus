```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): Input list of strings
        prefix (str): Prefix to filter by

    Returns:
        List[str]: Filtered list of strings that start with the given prefix
    """
    # Use list comprehension to create a new list that includes only strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list that includes only the strings from the input list that start with the given prefix. The function uses the `startswith` method of the string class to check if each string starts with the prefix. The example usage at the bottom demonstrates how to use the function with the input you provided in the docstring.