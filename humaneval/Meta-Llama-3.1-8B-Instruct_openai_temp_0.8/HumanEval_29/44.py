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
    # Use a list comprehension to filter the input list
    # The if condition checks if each string starts with the given prefix
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    print(filter_by_prefix([], 'a'))  # Expected output: []
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This script defines a `filter_by_prefix` function that takes a list of strings and a prefix as input. It uses a list comprehension to filter the input list and returns the filtered list of strings that start with the given prefix. The test cases at the end of the script demonstrate the function's behavior with different inputs.