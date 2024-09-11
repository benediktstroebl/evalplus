```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: The filtered list of strings.

    Example:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings_list = ['abc', 'bcd', 'cde', 'array', 'abcd']
prefix = 'a'
print(filter_by_prefix(strings_list, prefix))  # Output: ['abc', 'array', 'abcd']
```

In this script, we define a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to create the filtered list. The `startswith` method of the string class is used to check if a string starts with a given prefix. The script also includes example usage of the function.