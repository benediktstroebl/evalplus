```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    
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
    # Use a list comprehension to filter the strings
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    return filtered_strings

# Test the function
print(filter_by_prefix([], 'a'))  # Should print []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Should print ['abc', 'array']
print(filter_by_prefix(['hello', 'world', 'python'], 'py'))  # Should print ['python']
```

This script defines the `filter_by_prefix` function, which filters a list of strings based on a given prefix. It uses a list comprehension to achieve this, which is a concise way to create lists in Python. The script then tests the function with some examples to demonstrate its usage.