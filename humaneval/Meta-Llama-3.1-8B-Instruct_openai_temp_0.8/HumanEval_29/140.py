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
    """
    # Use a list comprehension to filter the strings
    # The 'if' condition checks if each string starts with the given prefix
    return [s for s in strings if s.startswith(prefix)]

# Example usage:
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # ['abc', 'array']
```

This script defines the `filter_by_prefix` function and includes example usage at the end. It uses a list comprehension to filter the input list of strings, which is a concise and efficient way to create a new list from an existing one. The `startswith` method is used to check if each string starts with the given prefix.