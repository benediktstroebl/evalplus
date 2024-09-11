```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    - strings (List[str]): A list of strings to be filtered.
    - prefix (str): The prefix to filter by.

    Returns:
    - List[str]: A list of strings that start with the given prefix.

    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Example usage:
strings = ['abc', 'bcd', 'cde', 'array', 'abcd']
prefix = 'a'
filtered_strings = filter_by_prefix(strings, prefix)
print(f"Strings with prefix '{prefix}': {filtered_strings}")
```

**Explanation:**

*   The `filter_by_prefix` function takes in a list of strings `strings` and a prefix `prefix`.
*   It uses a list comprehension to create a new list that includes only the strings from `strings` that start with the `prefix`.
*   The `startswith` method is used to check if a string starts with the given prefix.
*   The resulting list of filtered strings is returned.
*   In the example usage, we demonstrate how to use the function by filtering a list of strings with the prefix 'a'.