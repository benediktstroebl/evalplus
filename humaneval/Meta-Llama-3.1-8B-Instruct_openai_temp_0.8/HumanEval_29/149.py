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
    return [s for s in strings if s.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Filtered strings starting with '{prefix}': {filtered_strings}")
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix using a list comprehension. It then demonstrates the function's usage with a sample list of strings and a prefix.