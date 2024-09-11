```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): A list of strings to filter.
    prefix (str): A prefix to filter by.

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
strings_to_filter = ['abc', 'bcd', 'cde', 'array', 'xaz', 'yzb']
prefix_to_filter_by = 'a'

filtered_strings = filter_by_prefix(strings_to_filter, prefix_to_filter_by)

print(filtered_strings)
```

This script defines the `filter_by_prefix` function, which uses a list comprehension to filter the input list of strings based on whether they start with the given prefix. The function is then used to filter a list of strings, and the result is printed to the console.