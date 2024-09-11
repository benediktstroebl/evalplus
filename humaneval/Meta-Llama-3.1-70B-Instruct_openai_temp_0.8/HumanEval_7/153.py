```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): A substring to filter the list by.

    Returns:
    List[str]: A filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Example use cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
```

In this script, we're using a list comprehension to create a new list containing only the strings from the input list that contain the specified substring. The `in` operator checks if the substring is present in each string. If the substring is found, the string is included in the output list.