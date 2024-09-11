```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered
    substring (str): The substring to search for

    Returns:
    List[str]: A list of strings containing the given substring
    """
    # Use list comprehension to filter the list in a concise and efficient way
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters a list of strings based on whether they contain a given substring. The function uses list comprehension to create a new list with only the strings that contain the substring. The test cases at the end demonstrate the function's behavior.