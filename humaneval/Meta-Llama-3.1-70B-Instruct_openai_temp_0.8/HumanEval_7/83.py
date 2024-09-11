```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
print(filter_by_substring([], 'a'))  # Output: []
```

This script defines a function `filter_by_substring` that uses a list comprehension to filter a list of strings. The function checks if each string contains the given substring using the `in` operator. If the substring is found, the string is included in the output list. The function returns an empty list if the input list is empty or if no strings contain the substring.