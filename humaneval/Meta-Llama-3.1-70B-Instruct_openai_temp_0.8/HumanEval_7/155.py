```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

# Additional test cases for edge cases
assert filter_by_substring(['hello', 'world'], '') == ['hello', 'world']
assert filter_by_substring(['hello', 'world'], 'h') == ['hello']
assert filter_by_substring(['hello', 'world'], 'o') == ['hello', 'world']
assert filter_by_substring(['hello', 'world'], 'x') == []
```