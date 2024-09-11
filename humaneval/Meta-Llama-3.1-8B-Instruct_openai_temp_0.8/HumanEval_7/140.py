```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to search for.

    Returns:
    List[str]: A list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world'], 'o'))  # ['hello', 'world']
print(filter_by_substring(['hello', 'world'], 'xyz'))  # []
```

In this script, the function `filter_by_substring` uses list comprehension to create a new list that only includes the strings from the input `strings` list that contain the given `substring`. The example usage demonstrates how to use the function with different inputs.