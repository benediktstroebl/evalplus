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
    # Use a list comprehension to create a new list that includes only strings that start with the prefix
    filtered_strings = [string for string in strings if string.startswith(prefix)]
    
    return filtered_strings


# Test the function
if __name__ == "__main__":
    # Test case 1: Empty list
    print(filter_by_prefix([], 'a'))  # Expected output: []

    # Test case 2: List with strings that start with the prefix and others that don't
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This code defines the `filter_by_prefix` function that takes in a list of strings and a prefix, and returns a new list that includes only the strings that start with the given prefix. The function uses a list comprehension to achieve this. The test cases are included in the code to demonstrate the function's usage.