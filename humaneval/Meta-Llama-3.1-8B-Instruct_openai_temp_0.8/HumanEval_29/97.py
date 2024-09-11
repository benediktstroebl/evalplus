```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The input list of strings to be filtered.
    prefix (str): The prefix to filter the input list with.

    Returns:
    List[str]: The filtered list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


# Example usage
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
    print(filter_by_prefix(['hello', 'world', 'python', 'programming'], 'p'))  # ['python', 'programming']
```

This Python script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. The function uses a list comprehension to iterate over the input list, checking each string to see if it starts with the given prefix using the `startswith` method. If a string matches the prefix, it is included in the filtered list. The script also includes example usage to demonstrate the function's behavior.