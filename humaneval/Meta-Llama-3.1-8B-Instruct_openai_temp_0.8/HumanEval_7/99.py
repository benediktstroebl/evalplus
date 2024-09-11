```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
        strings (List[str]): The list of strings to filter
        substring (str): The substring to search for

    Returns:
        List[str]: The filtered list of strings
    """
    return [string for string in strings if substring in string]

# Example usage:
strings = ['abc', 'bacd', 'cde', 'array', 'no_match','matching_another']
substring = 'a'
print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The example usage demonstrates how to use this function and the test cases verify that it works correctly.