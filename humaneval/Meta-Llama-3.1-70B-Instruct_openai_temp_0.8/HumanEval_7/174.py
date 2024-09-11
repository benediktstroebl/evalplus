```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The input list of strings.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A new list containing only the strings that contain the substring.
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']

# Additional test cases for edge cases
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], ''))  # ['abc', 'bacd', 'cde', 'array']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'))  # []
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter the input list of strings. It checks if the substring is present in each string using the `in` operator, and includes only the strings that contain the substring in the output list. The script also includes test cases to demonstrate the function's behavior.