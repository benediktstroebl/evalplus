```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.

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

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to iterate over the input list and includes only the strings that match the prefix. The example usage at the end shows how to use the function with a sample list of strings and prefix.