```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to filter
        substring (str): The substring to search for in each string

    Returns:
        List[str]: A new list containing only the strings that contain the substring

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    # Use list comprehension to filter the input list
    # The 'if' condition inside the list comprehension checks if the substring is in each string
    return [string for string in strings if substring.lower() in string.lower()]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

In this script, we use a list comprehension to create a new list that only includes the strings from the input list that contain the specified substring. The `if` condition inside the list comprehension checks if the substring (converted to lowercase for case-insensitive comparison) is a substring of each string (also converted to lowercase).

This script provides a clear and concise implementation of the `filter_by_substring` function, along with an example usage and documentation.