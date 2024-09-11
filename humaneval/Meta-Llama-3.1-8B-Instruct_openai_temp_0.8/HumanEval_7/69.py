```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter
        substring (str): The substring to search for

    Returns:
        List[str]: A new list containing the strings that contain the given substring
    """
    # Use a list comprehension to create a new list that includes only the strings
    # that contain the given substring
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array']
substring = 'a'
print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```

This Python script defines a function called `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list that includes only the strings from the input list that contain the given substring. The function uses a list comprehension for efficient filtering, and includes docstrings and example usage for clarity and readability.