```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): Input list of strings
        substring (str): Substring to search in strings

    Returns:
        List[str]: Filtered list of strings
    """
    return [string for string in strings if substring in string]

# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. The function uses a list comprehension for efficient filtering. The example usage demonstrates how to use the function with the given test cases.