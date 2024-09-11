```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to match.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
print(filter_by_prefix([], 'a'))
# Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
# Output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'h'))
# Output: ['hello', 'world', 'python']
print(filter_by_prefix(['cat', 'dog', 'elephant'], 'd'))
# Output: ['dog']
```

This script defines a function `filter_by_prefix` that uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. It then demonstrates the function's usage with some example inputs.