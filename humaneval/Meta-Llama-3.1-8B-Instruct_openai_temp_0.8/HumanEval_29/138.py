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

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['apple', 'banana', 'cherry'], 'b'))  # Output: ['banana']
```