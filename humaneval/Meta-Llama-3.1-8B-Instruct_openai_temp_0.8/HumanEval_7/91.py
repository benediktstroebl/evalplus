```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The input list of strings
        substring (str): The substring to search for

    Returns:
        List[str]: The filtered list of strings
    """
    # Use list comprehension to create a new list that includes only the strings 
    # that contain the given substring
    return [string for string in strings if substring in string]

# Test the function
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python'], 'o'))  # ['hello', 'world']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list that includes only the strings that contain the given substring. It uses list comprehension to create the new list, which is a concise and efficient way to create lists in Python. The function is then tested with some example inputs.