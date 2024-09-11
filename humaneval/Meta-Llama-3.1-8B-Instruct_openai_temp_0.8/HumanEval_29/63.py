```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings
        prefix (str): The prefix to filter by

    Returns:
        List[str]: A list of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
```

This script defines the `filter_by_prefix` function, which uses a list comprehension to filter the input list of strings. The `startswith` method is used to check if each string starts with the given prefix. The function returns the filtered list of strings.

The example usage at the end shows how to use the function with the provided test cases.