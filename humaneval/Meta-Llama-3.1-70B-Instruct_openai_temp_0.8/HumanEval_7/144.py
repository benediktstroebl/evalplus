```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to filter the input list of strings
    # The 'if substring in string' condition ensures only strings containing the substring are included
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that include the given substring. The function uses list comprehension to achieve this in a concise and readable manner.