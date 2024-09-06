Here is a self-contained Python script that implements the provided function filter_by_prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Parameters:
    strings (List[str]) - List of strings
    prefix - String to search for in the strings.

    Returns: filtered list of strings that start with the given prefix.

    Test cases:
    >>> test_list = ['abc', 'bcd', 'cde', 'array', 'hello']
    >>> filter_by_prefix(test_list, 'cde')
    ['cde']
    """
    return [string for string in strings if string.startswith(prefix)]
```
This function is designed to take a list of strings and a prefix as parameters, and it will return a new list that contains only the strings from the input list that start with the given prefix. 

It utilizes a powerful typing system in Python and a list comprehension to achieve this. This makes the function self-contained and easy to understand.