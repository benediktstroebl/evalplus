```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: The filtered list of strings.

    Example:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Testing the function
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
    print(filter_by_prefix(['hello', 'world', 'python', 'programming'], 'p'))
```

In this script, the `filter_by_prefix` function uses list comprehension to filter the input list of strings. It uses the `startswith` method of the string class to check if each string starts with the given prefix. The result is a new list containing only the strings that start with the prefix. The script also includes example usage of the function.