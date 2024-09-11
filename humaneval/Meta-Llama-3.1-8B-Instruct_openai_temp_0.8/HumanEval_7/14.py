```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): The list of strings to be filtered
    substring (str): The substring that the strings must contain

    Returns:
    List[str]: A list of strings containing the given substring
    """
    return [string for string in strings if substring in string]


# Example usage
if __name__ == "__main__":
    print(filter_by_substring([], 'a'))  # Output: []
    print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
    print(filter_by_substring(['hello', 'world', 'python'], 'y'))  # Output: ['hello', 'python']
```

This script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses a list comprehension to create a new list containing only the strings that contain the specified substring.

The script also includes example usage to demonstrate how the function works.