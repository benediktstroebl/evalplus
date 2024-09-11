```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring that must be present in the strings
        
    Returns:
        List[str]: The filtered list of strings
        
    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. The function uses a list comprehension to achieve this. The script also includes example usage of the function.