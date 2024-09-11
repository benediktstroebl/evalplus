```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The input list of strings
        prefix (str): The prefix to filter by

    Returns:
        List[str]: The filtered list of strings

    Examples:
        >>> filter_by_prefix([], 'a')
        []
        >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
        ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]


# Example usage:
if __name__ == "__main__":
    strings = ['abc', 'bcd', 'cde', 'array']
    prefix = 'a'
    result = filter_by_prefix(strings, prefix)
    print(result)  # Output: ['abc', 'array']
```

This script defines the `filter_by_prefix` function and includes example usage. It uses a list comprehension to filter the input list `strings` based on whether each string starts with the given `prefix`. The result is printed to the console.