```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the list of strings
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    return filtered_strings

# Example usage:
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This script implements the `filter_by_prefix` function as specified and includes example usage to demonstrate its functionality. It uses list comprehension to efficiently filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method is used to check if a string starts with a particular prefix.