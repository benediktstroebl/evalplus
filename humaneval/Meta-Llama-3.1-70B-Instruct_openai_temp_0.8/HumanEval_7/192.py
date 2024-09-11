```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to filter by

    Returns:
        List[str]: A new list containing only the strings that have the substring
    """
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that have the substring. It uses a list comprehension to create the new list. The test cases at the end verify that the function works as expected.