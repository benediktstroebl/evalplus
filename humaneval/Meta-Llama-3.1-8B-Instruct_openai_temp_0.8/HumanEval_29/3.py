```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A filtered list of strings.

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(filtered_strings)  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses a list comprehension to create a new list containing only the strings that start with the given prefix. The function is then tested with an example usage.