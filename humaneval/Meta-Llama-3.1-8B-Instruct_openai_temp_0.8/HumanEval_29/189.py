```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): The list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A list of strings that start with the given prefix.
    """
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Expected output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that uses a list comprehension to filter the input list `strings` for strings that start with the given `prefix`. The `startswith` method of the string class is used to check if a string starts with a given prefix. The test cases at the end of the script demonstrate the function's behavior.