### Filter Strings by Prefix
#### Python Script
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

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage
strings = ['abc', 'bcd', 'cde', 'array', 'prefix_test', 'test_prefix']
prefix = 'pre'
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Filtered strings with prefix '{prefix}': {filtered_strings}")
```

In this script, we define a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to filter the input list. We also include an example usage of the function to demonstrate its behavior.