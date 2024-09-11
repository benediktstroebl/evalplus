```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]

# Test cases
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python', 'development'], 'p'))  # ['python', 'development']
print(filter_by_prefix(['apple', 'banana', 'cherry', 'date'], 'b'))  # ['banana']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to achieve this. The test cases at the end of the script demonstrate the function's behavior with different inputs.