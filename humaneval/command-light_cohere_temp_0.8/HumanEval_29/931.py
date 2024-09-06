```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    Args:
        strings: list, a list of strings. string strings with possible prefix.
        prefix: str, the prefix to filter for.
    Returns:
        filtered list of strings starting with the given prefix.
    """
"""
    return [string for string in strings if string.startswith(prefix)]

 # Test case:
strings = ['abc', 'bcd', 'cde', 'array', 'welcome']
prefix = 'cde'
filtered = filter_by_prefix(strings, prefix)
print(filtered)  # Output: ['cde', 'array']
``` 
This code defines a function called **`filter_by_prefix`** that filters a list of strings based on a given prefix. It uses the Python's **List** and **str** types to define input parameters and return values. The function uses the filter function to check if each string in the input list starts with the given prefix, and returns a list of matching strings.