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
    """
    # Use list comprehension to create a new list with strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]


# Test cases
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'py'))  # ['python']
print(filter_by_prefix(['apple', 'banana', 'cherry'], 'd'))  # []
print(filter_by_prefix([], 'test'))  # []
```

This script defines the `filter_by_prefix` function and includes several test cases to demonstrate its usage. The function uses list comprehension to efficiently filter the input list based on the provided prefix. The `startswith` method is used to check if each string in the list starts with the given prefix.