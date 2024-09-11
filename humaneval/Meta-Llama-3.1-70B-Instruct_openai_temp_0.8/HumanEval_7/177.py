```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings to filter.
        substring (str): Substring to search for in the input list.

    Returns:
        List[str]: Filtered list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that uses list comprehension to filter the input list of strings based on the presence of a given substring. The function includes a docstring that describes its purpose, parameters, and return value. The script also includes test cases to demonstrate its usage.