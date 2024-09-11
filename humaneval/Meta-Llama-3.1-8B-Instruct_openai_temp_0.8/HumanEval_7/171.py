```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to search for in the strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """

    # Use list comprehension to filter strings that contain the substring
    filtered_strings = [string for string in strings if substring in string]

    # Return the filtered list of strings
    return filtered_strings

# Example usage:
if __name__ == "__main__":
    # Test case 1: empty list
    print(filter_by_substring([], 'a'))  # Expected output: []

    # Test case 2: non-empty list with some strings containing the substring
    strings = ['abc', 'bacd', 'cde', 'array']
    print(filter_by_substring(strings, 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. It uses list comprehension to create a new list that only includes strings that contain the substring. The function includes docstrings to describe its behavior and parameters. The script also includes example usage to demonstrate how to use the function.