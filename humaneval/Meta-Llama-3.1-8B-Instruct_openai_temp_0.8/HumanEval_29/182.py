```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the strings
    # The 'if' condition checks if each string starts with the given prefix
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    return filtered_strings

# Test cases
print(filter_by_prefix([], 'a'))  # Expected output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines the `filter_by_prefix` function as specified, which filters a list of strings based on a given prefix. The function uses list comprehension to efficiently create a new list containing only the strings that start with the prefix. The test cases at the end demonstrate the function's behavior with different inputs.