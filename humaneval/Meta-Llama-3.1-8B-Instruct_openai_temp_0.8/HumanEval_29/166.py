```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): Input list of strings
        prefix (str): Prefix to filter by

    Returns:
        List[str]: Filtered list of strings
    """
    return [string for string in strings if string.startswith(prefix)]

# Example usage
print(filter_by_prefix([], 'a'))  # Output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Output: ['abc', 'array']
```

This Python script defines a function `filter_by_prefix` that uses list comprehension to filter the input list of strings based on whether each string starts with the given prefix. The `startswith` method is used to check if a string starts with a given prefix. If the prefix is an empty string, the function will return the original list of strings.