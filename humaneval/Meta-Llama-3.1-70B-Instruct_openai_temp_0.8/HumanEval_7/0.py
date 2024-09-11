### Filtering a List of Strings by Substring
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): Input list of strings.
        substring (str): Substring to filter by.

    Returns:
        List[str]: List of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    empty_list = []
    list_with_substring = ['abc', 'bacd', 'cde', 'array']

    print(filter_by_substring(empty_list, 'a'))  # Expected output: []
    print(filter_by_substring(list_with_substring, 'a'))  # Expected output: ['abc', 'bacd', 'array']
```
In this code:

*   We define a function `filter_by_substring` that takes a list of strings and a substring as input.
*   It uses a list comprehension to create a new list containing only the strings that have the given substring.
*   We include example usage in the `if __name__ == "__main__":` block to demonstrate how the function works.

This script can be saved to a file (e.g., `filter_by_substring.py`) and run directly with Python (e.g., `python filter_by_substring.py`).