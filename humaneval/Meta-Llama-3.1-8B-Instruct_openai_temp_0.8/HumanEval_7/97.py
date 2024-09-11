```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to filter from
    substring (str): The substring to search for in the list

    Returns:
    List[str]: A list of strings that contain the given substring

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
filtered = filter_by_substring(strings, substring)

print(f"Strings containing '{substring}': {filtered}")
```

This Python script defines a function `filter_by_substring` that filters a list of strings to include only those that contain a specified substring. The function uses a list comprehension to create a new list that meets the filtering criteria. The example usage demonstrates how to call the function and print the result.