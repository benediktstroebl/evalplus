```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): A prefix to filter the strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(['hello', 'world'], 'world'))  # Output: ['world']
    print(filter_by_prefix(['a', 'aa', 'aaa'], 'a'))  # Output: ['a', 'aa', 'aaa']
```

This script defines a function `filter_by_prefix` that uses list comprehension to create a new list containing only the strings from the input list that start with the given prefix. The `startswith` method of the `str` class is used to check if a string starts with the given prefix. The script also includes example usage to demonstrate how to use the function.