### Filter Strings by Prefix
#### Python Script
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): The input list of strings.
    - prefix (str): The prefix to filter by.

    Returns:
    - List[str]: The filtered list of strings.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'xyz']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Strings starting with '{prefix}': {filtered_strings}")
```
This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses a list comprehension to filter the input list and return a new list containing only the strings that start with the given prefix. The function is then demonstrated in an example usage section.