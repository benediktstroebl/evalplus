```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): A list of strings to be filtered.
    substring (str): The substring to be searched in the strings.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]

# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a list of strings that contain the given substring. It uses list comprehension to achieve this in a concise and readable way. The test cases are also included to verify the correctness of the function.