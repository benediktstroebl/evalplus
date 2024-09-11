```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world'], 'h'))  # Expected output: ['hello']
print(filter_by_prefix(['cat', 'dog', 'elephant'], 'e'))  # Expected output: ['elephant']
```

This script defines a function `filter_by_prefix` that uses a list comprehension to filter the input list `strings` based on whether each string `s` starts with the given prefix. The function returns the filtered list of strings. The script then demonstrates the function's usage with several test cases.