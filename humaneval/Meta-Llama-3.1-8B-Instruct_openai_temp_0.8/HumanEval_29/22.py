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

    Example:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]

# Test the function
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
    print(filter_by_prefix(['hello', 'world', 'python', 'code'], 'py'))  # Output: ['python', 'code']
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. The function uses a list comprehension to achieve this. The script also includes example test cases to demonstrate the function's behavior.