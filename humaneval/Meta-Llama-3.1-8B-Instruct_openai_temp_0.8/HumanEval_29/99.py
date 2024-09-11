```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: The list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage
strings_list = ['abc', 'bcd', 'cde', 'array', 'abcd', 'efg']
prefix = 'a'
filtered_list = filter_by_prefix(strings_list, prefix)
print(f"Strings that start with '{prefix}': {filtered_list}")
```
In this code, we define a function `filter_by_prefix` that uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method of the string is used to check if the prefix is at the beginning of the string.