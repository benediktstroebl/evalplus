```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Test cases
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'w'))  # Output: ['world']
print(filter_by_prefix(['apple', 'banana', 'cherry'], 'b'))  # Output: ['banana']
print(filter_by_prefix(['a', 'aa', 'aaa'], 'a'))  # Output: ['a', 'aa', 'aaa']
```

This script defines the `filter_by_prefix` function as a list comprehension that iterates over the input list of strings and checks if each string starts with the given prefix. It returns a new list containing only the strings that start with the prefix. The test cases demonstrate the function's behavior with different inputs.