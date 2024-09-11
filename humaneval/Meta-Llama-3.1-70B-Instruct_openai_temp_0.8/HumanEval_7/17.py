```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to search for in the strings.

    Returns:
        List[str]: A new list containing only the strings that include the substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that uses a list comprehension to create a new list containing only the strings from the input list that include the specified substring. The function is then tested with two example use cases.