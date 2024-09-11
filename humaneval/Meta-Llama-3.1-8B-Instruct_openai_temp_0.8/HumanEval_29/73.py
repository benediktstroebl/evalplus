```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    # Use list comprehension to filter the input list
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'c'))  # Output: ['cde']
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], ''))  # Output: ['abc', 'bcd', 'cde', 'array']
```

In this script, I used list comprehension to filter the input list `strings`. The `startswith()` method is used to check if each string in the list starts with the given `prefix`. This method returns `True` if the string starts with the prefix, and `False` otherwise. The list comprehension then includes only the strings for which `startswith()` returns `True`.