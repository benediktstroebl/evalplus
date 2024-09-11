```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered.
        substring (str): The substring to search for.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to create a new list with only the strings that contain the substring
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

This script defines the `filter_by_substring` function, which uses list comprehension to filter a list of strings based on whether they contain a given substring. The function is then tested with the provided example inputs.