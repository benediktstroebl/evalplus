```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input. It uses a list comprehension to create a new list that only includes the strings from the input list that contain the given substring.

The function is then tested with two test cases: an empty list and a list of strings with some containing the substring 'a' and some not. The expected output for each test case is printed to the console.