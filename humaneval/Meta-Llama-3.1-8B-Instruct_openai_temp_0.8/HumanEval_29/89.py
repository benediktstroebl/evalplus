```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): A list of strings to be filtered.
    prefix (str): The prefix that strings in the output list should start with.

    Returns:
    List[str]: A list of strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)]


# Example usage:
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to filter the input list. The script also includes example usage to demonstrate how to use the function.