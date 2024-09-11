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

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'xyz']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Strings starting with '{prefix}': {filtered_strings}")
```

This Python script defines a `filter_by_prefix` function that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. It uses a list comprehension to filter the input list based on the `startswith` method. The script includes example usage at the end to demonstrate how to call the function and print the result.