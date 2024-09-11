```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings (List[str]): A list of strings to be filtered.
    prefix (str): The prefix that strings must start with.

    Returns:
    List[str]: A list of strings that start with the given prefix.
    """
    return [string for string in strings if string.startswith(prefix)]


# Test cases
if __name__ == "__main__":
    print("Test case 1: Empty list")
    print(filter_by_prefix([], 'a'))

    print("\nTest case 2: List with elements that start with the prefix")
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))

    print("\nTest case 3: List with elements that do not start with the prefix")
    print(filter_by_prefix(['abc', 'bcd', 'cde', 'def'], 'a'))
```

In this script, the `filter_by_prefix` function uses list comprehension to create a new list that includes only the strings that start with the given prefix. The `startswith` method is used to check if a string starts with a given prefix. The test cases are included at the end to demonstrate the function's behavior.