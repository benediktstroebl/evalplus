```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring that the strings should contain.

    Returns:
    List[str]: The list of strings that contain the given substring.

    Examples:
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
```

In this script, the `filter_by_substring` function uses a list comprehension to create a new list containing only the strings from the input list that contain the given substring. The function is then tested with the provided examples.