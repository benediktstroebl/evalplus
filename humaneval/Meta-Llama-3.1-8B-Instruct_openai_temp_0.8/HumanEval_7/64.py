```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring that needs to be present in strings
    
    Returns:
        List[str]: A list of strings that contain the given substring
    
    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world'], 'or'))  # ['world']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'))  # []
```

This script uses a list comprehension to filter the input list of strings, keeping only the ones that contain the given substring. It then includes test cases to demonstrate the function's behavior.