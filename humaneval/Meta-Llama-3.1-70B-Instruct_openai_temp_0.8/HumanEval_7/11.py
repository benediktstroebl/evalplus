```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to look for in the strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    # Use list comprehension to create a new list with strings that contain the substring
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function as specified, along with two test cases to verify its correctness. The function uses a list comprehension to create a new list that includes only the strings from the input list that contain the given substring.