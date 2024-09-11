```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): The list of strings to filter.
        substring (str): The substring to filter by.

    Returns:
        List[str]: A new list containing only the strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']

# Test cases:
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello', 'world', 'hello world'], 'hello') == ['hello', 'hello world']
assert filter_by_substring(['apple', 'banana', 'orange'], 'pear') == []
```