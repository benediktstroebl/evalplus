```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    
    Args:
    strings (List[str]): The list of strings to be filtered.
    substring (str): The substring to filter by.
    
    Returns:
    List[str]: The list of strings that contain the given substring.
    
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)
```

This script uses a list comprehension to filter the input list of strings based on whether each string contains the given substring. The `in` operator is used to check if a string contains the substring. The result is a new list containing only the strings that meet the condition.