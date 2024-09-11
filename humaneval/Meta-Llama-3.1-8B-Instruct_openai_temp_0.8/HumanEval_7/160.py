```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to search for in each string.

    Returns:
        List[str]: A list of strings that contain the given substring.

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test cases
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['apple', 'banana', 'cherry'], 'an'))
print(filter_by_substring(['hello', 'world', 'python'], 'z'))
```

This script defines the `filter_by_substring` function which uses a list comprehension to create a new list containing only the strings from the input list that contain the given substring. The function includes docstrings to provide documentation and examples. The script also includes some test cases to demonstrate the function's behavior.