```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.
    
    Args:
    strings (List[str]): The list of strings to filter.
    substring (str): The substring to search for.
    
    Returns:
    List[str]: A new list containing only the strings that contain the substring.
    """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script uses list comprehension to create a new list containing only the strings from the input list that contain the given substring. The `in` operator is used to check if the substring is present in each string.