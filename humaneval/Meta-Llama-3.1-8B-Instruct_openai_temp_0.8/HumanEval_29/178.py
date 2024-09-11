```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to filter.
        prefix (str): The prefix to filter by.

    Returns:
        List[str]: The filtered list of strings.
    """
    return [string for string in strings if string.startswith(prefix)]

# Test cases
if __name__ == "__main__":
    # Test case 1: Empty list with prefix 'a'
    print(filter_by_prefix([], 'a'))  # Expected output: []

    # Test case 2: List with prefix 'a'
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'array']
```

This Python script defines the `filter_by_prefix` function, which uses a list comprehension to filter the input list `strings` for strings that start with the given `prefix`. The function returns the filtered list. The script includes two test cases to demonstrate the function's usage.