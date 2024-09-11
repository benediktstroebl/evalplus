```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring to filter the strings by.

    Returns:
        List[str]: A list of strings containing the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
print(filter_by_substring([], 'a'))  # []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # ['abc', 'bacd', 'array']

# More test cases for edge cases
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], ''))  # ['abc', 'bacd', 'cde', 'array']
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z'))  # []
print(filter_by_substring(['a', 'aa', 'aaa'], 'a'))  # ['a', 'aa', 'aaa']
```