```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    
    Args:
    strings (List[str]): A list of strings to filter
    substring (str): The substring to search for
    
    Returns:
    List[str]: A list of strings containing the given substring
    
    Example:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['hello', 'world', 'python', 'programming'], 'o'))
```

This script defines a function `filter_by_substring` that filters a list of strings based on whether each string contains a given substring. The function uses a list comprehension to create a new list containing only the strings that match the filter condition. The script then includes example use cases to demonstrate how the function works.