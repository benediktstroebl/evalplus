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


# Example usage
strings_list = ['abc', 'bcd', 'cde', 'array', 'xyz']
prefix_to_filter = 'a'
filtered_list = filter_by_prefix(strings_list, prefix_to_filter)

print(f"Filtering list '{strings_list}' with prefix '{prefix_to_filter}':")
print(filtered_list)
```

This code defines the `filter_by_prefix` function as requested, which takes a list of strings and a prefix as input. It uses a list comprehension to return a new list containing only the strings that start with the given prefix. The function is accompanied by a docstring that provides a clear description of its behavior, as well as some example usage at the end.