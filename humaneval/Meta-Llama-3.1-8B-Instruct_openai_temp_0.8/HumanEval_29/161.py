```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): Input list of strings.
        prefix (str): Prefix to filter by.

    Returns:
        List[str]: Filtered list of strings.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    # Use a list comprehension to filter the input list
    # The 'if' condition in the list comprehension checks if each string starts with the given prefix
    return [s for s in strings if s.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```