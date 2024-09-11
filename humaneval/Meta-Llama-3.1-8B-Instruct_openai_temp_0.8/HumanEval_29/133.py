```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.

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

In this script, the `filter_by_prefix` function uses a list comprehension to create a new list that includes only the strings from the input list that start with the given prefix. The `startswith` method is used to check if a string starts with the prefix. The example usage at the end demonstrates how to use this function with a list of strings and a prefix.