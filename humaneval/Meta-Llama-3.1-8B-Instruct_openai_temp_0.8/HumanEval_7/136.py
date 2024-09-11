```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    
    Args:
    strings (List[str]): The list of strings to filter.
    substring (str): The substring to search for in the strings.
    
    Returns:
    List[str]: The filtered list of strings containing the substring.
    
    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This script defines a function `filter_by_substring` that filters a list of strings based on the presence of a given substring. It uses a list comprehension to create a new list containing only the strings that contain the substring. The function is then tested with the provided examples.