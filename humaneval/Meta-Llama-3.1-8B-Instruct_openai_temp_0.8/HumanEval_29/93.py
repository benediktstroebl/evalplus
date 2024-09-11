```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): A list of strings to be filtered.
        prefix (str): The prefix to filter the strings by.

    Returns:
        List[str]: A filtered list of strings that start with the given prefix.
    """
    # Use list comprehension to create a new list containing strings that start with the prefix
    return [string for string in strings if string.startswith(prefix)]


# Test cases
if __name__ == "__main__":
    # Test case 1: empty list
    assert filter_by_prefix([], 'a') == []

    # Test case 2: non-empty list
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
```

This script defines the `filter_by_prefix` function, which uses list comprehension to filter the input list `strings` for strings that start with the given `prefix`. The function returns the filtered list.

The script also includes two test cases to verify that the function works correctly. The `if __name__ == "__main__":` block ensures that the test cases are only executed when the script is run directly (not when it's imported as a module by another script).