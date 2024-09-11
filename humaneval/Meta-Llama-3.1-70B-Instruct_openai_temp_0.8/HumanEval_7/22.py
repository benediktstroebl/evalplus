```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): Input list of strings to filter.
    substring (str): Substring to filter by.

    Returns:
    List[str]: Filtered list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
```

This script uses a list comprehension to filter the input list of strings. It checks if the given substring is present in each string and includes it in the output list if it is. The test cases are included to verify the correctness of the function.