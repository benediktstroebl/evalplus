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

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]


# Test the function
if __name__ == "__main__":
    strings = ['abc', 'bcd', 'cde', 'array']
    prefix = 'a'
    filtered_strings = filter_by_prefix(strings, prefix)
    print(f"Filtering '{prefix}' from '{strings}' gives: {filtered_strings}")
```

This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses list comprehension to achieve this in a concise manner.

The script also includes a test case to demonstrate how to use the function and verify its correctness. The test case filters the list `['abc', 'bcd', 'cde', 'array']` with the prefix `'a'` and prints the result.