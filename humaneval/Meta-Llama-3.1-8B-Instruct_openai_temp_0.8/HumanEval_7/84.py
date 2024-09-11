```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to filter
        substring (str): The substring to search for

    Returns:
        List[str]: A list of strings that contain the given substring
    """
    # Use a list comprehension to filter the input list
    return [string for string in strings if substring in string]

# Example use cases:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The function uses a list comprehension to achieve this, which is a concise and efficient way to create a new list by iterating over the input list. The example use cases demonstrate the function's behavior with empty input and a non-empty input list.