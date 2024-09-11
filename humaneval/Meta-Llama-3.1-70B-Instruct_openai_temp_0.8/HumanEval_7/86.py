```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The list of input strings.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A new list containing only the strings that include the substring.
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This Python script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that include the given substring. The function uses a list comprehension to filter the input list. The script also includes test cases to verify the function's behavior.