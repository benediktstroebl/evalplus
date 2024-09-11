```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): A substring to filter by.

    Returns:
        List[str]: A filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses list comprehension to create a new list containing only the strings that have the specified substring. The function takes a list of strings and a substring as input and returns the filtered list.

The test cases at the end of the script verify that the function works correctly for an empty list and a list with some matching strings.