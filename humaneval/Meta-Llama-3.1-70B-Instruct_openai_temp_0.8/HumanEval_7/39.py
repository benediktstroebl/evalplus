```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A new list containing only the strings that contain the substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b'))  # Expected: ['abc', 'bacd']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'd'))  # Expected: ['bacd', 'cde']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'e'))  # Expected: ['cde']
```
This Python script defines a function `filter_by_substring` that uses a list comprehension to filter a list of strings based on the presence of a given substring. The function is then tested with several test cases to ensure it works correctly.