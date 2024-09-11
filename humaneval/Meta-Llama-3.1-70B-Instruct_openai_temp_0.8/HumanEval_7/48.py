```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to filter.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A new list containing only the strings that contain the substring.
    """
    return [string for string in strings if substring in string]


# Example use cases:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

This script uses a list comprehension to filter the input list of strings. It iterates over each string in the input list, checks if the substring is present in the string using the `in` operator, and includes the string in the output list if the substring is found. The resulting list is then returned by the function.