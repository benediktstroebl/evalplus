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
    # Use list comprehension to create a new list with strings that start with the prefix
    # The 'if' condition in the list comprehension checks if each string starts with the prefix
    return [string for string in strings if string.startswith(prefix)]

# Example usage:
if __name__ == "__main__":
    # Test cases
    print(filter_by_prefix([], 'a'))  # Expected output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a function `filter_by_prefix` that filters a list of strings based on a given prefix. It uses list comprehension to create a new list with strings that start with the prefix. The example usage section demonstrates how to use the function with test cases. The `if __name__ == "__main__":` block ensures that the test cases are only executed when the script is run directly.