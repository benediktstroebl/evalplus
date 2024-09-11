```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
    strings (List[str]): List of strings to filter
    substring (str): The substring to search for
    
    Returns:
    List[str]: List of strings that contain the given substring
    
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The function is then tested with some example usage.