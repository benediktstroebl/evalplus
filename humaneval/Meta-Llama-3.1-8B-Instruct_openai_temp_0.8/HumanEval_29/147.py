```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix that a string should start with to be included in the result.

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
if __name__ == "__main__":
    strings = ['abc', 'bcd', 'cde', 'array']
    prefix = 'a'
    filtered_strings = filter_by_prefix(strings, prefix)
    print(f"Strings starting with '{prefix}': {filtered_strings}")
```

In this script, we define a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses a list comprehension to create a new list that includes only the strings that start with the given prefix. The `startswith` method of Python strings is used to check if a string starts with a given prefix. We then demonstrate the usage of this function with an example.