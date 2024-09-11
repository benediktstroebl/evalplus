```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered
    substring (str): A substring to search for in the input strings

    Returns:
    List[str]: A list of strings that contain the given substring

    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
print(filter_by_substring(['apple', 'banana', 'cherry'], 'an'))  # Expected output: ['banana']
```

This Python script uses a list comprehension to create a new list containing only the strings from the input list that contain the given substring. The `in` operator is used to check if a string contains the substring. If the substring is found in a string, that string is included in the new list. If the substring is not found in any string, an empty list is returned.