```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of string inputs to filter.
        prefix (str): The prefix to search for in the input strings.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use a list comprehension to filter the input list
    # The if condition checks if each string starts with the given prefix
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to filter the input list, which is a concise and efficient way to create a new list from an existing list. The `startswith` method is used to check if each string starts with the given prefix. The script also includes two test cases to demonstrate the function's behavior.