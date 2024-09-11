```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    
    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix that the strings should start with.
    
    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use a list comprehension to create a new list with strings that start with the given prefix
    return [string for string in strings if string.startswith(prefix)]

# Test the function
print(filter_by_prefix([], 'a'))  # []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
```

This script defines the `filter_by_prefix` function as specified and includes test cases to demonstrate its usage. The function uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method is used to check if a string starts with a given prefix.