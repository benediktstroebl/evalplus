```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    
    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to search for in each string.
    
    Returns:
        List[str]: The filtered list of strings containing the given substring.
    
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered_strings = filter_by_substring(strings, substring)
print(filtered_strings)
```

In this script, a list comprehension is used to create a new list that includes only the strings from the input list that contain the given substring. The `in` operator is used to search for the substring in each string. If the substring is found, the string is included in the new list; otherwise, it is excluded.