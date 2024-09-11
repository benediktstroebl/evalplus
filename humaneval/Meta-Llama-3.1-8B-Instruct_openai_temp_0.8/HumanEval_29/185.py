```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): The list of strings to be filtered.
    prefix (str): The prefix to filter by.

    Returns:
    List[str]: A list of strings that start with the given prefix.

    Examples:
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


# Test the function
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
    print(filter_by_prefix(['hello', 'world', 'python', 'programming'], 'p'))  # ['python', 'programming']
    print(filter_by_prefix(['apple', 'banana', 'cherry'], 'a'))  # ['apple']
```

This script defines the `filter_by_prefix` function and includes test cases to demonstrate its usage. The function uses a list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method of the string class is used to check for the prefix.