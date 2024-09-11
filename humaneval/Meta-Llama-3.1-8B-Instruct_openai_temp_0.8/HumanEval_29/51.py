```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings.
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

This script defines a function `filter_by_prefix` that uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method is used to check if a string starts with a given prefix. The script also includes an example usage of the function in the `if __name__ == "__main__":` block.