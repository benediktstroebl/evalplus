```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to be filtered
        substring (str): The substring to filter by

    Returns:
        List[str]: The filtered list of strings
    """
    # Use list comprehension to create a new list containing only the strings that contain the substring
    return [string for string in strings if substring in string]


# Test cases
if __name__ == "__main__":
    # Test with empty list
    print(filter_by_substring([], 'a'))  # Expected output: []

    # Test with list containing strings with and without the substring
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The function uses list comprehension to achieve this. The script then includes test cases to verify that the function works as expected.