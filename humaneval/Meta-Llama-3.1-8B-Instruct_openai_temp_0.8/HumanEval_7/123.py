```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: The filtered list of strings

    Example:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]


# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['apple', 'banana', 'cherry'], 'an'))
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings from the input list that contain the given substring. The function uses a list comprehension to filter the input list, which is a concise and efficient way to create a new list from an existing list. The script also includes some example use cases to demonstrate how the function works.