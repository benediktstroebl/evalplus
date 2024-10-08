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
    """
    # Use a list comprehension to create a new list that includes only the strings
    # that start with the given prefix.
    return [string for string in strings if string.startswith(prefix)]


# Test cases
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
```

This script defines the `filter_by_prefix` function and includes test cases to demonstrate its usage. The function takes in a list of strings and a prefix, and returns a new list that includes only the strings that start with the given prefix. The test cases show that the function returns an empty list for an empty input list, and returns the expected filtered list for a non-empty input list.