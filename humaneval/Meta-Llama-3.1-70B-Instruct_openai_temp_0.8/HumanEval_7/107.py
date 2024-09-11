```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
    strings (List[str]): The input list of strings.
    substring (str): The substring to filter by.

    Returns:
    List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

# Additional test cases for edge cases
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], '') == ['abc', 'bacd', 'cde', 'array']
assert filter_by_substring([], '') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'd') == ['bacd']
```

This script defines the `filter_by_substring` function, which uses a list comprehension to filter the input list of strings. It checks if the given substring is present in each string and only includes the string in the output list if the substring is found.

The script also includes several test cases to verify that the function works correctly. The test cases cover different scenarios, including an empty input list, a list with strings that contain the substring, and edge cases like an empty substring.