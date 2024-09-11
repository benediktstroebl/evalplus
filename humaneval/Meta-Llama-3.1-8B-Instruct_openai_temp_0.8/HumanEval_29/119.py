```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Strings starting with '{prefix}': {filtered_strings}")
```

In this script, we define a function `filter_by_prefix` that uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The function then returns this filtered list. The example usage demonstrates how to use this function by filtering a list of strings based on a given prefix.