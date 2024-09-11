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
    # Use list comprehension to filter the strings based on the prefix
    return [string for string in strings if string.startswith(prefix)]


# Test cases
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Expected output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses list comprehension to create a new list containing only the strings that start with the given prefix. The `startswith` method is used to check if a string starts with the given prefix.

The script also includes test cases to demonstrate the function's behavior. The `if __name__ == "__main__":` block is used to ensure that the test cases are only run when the script is executed directly, not when it's imported as a module.