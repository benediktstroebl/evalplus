```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring

    Args:
    strings (List[str]): Input list of strings
    substring (str): Substring to filter by

    Returns:
    List[str]: Filtered list of strings containing the substring
    """
    return [s for s in strings if substring in s]


# Example usage:
print(filter_by_substring([], 'a'))  # Output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Output: ['abc', 'bacd', 'array']

# Test cases:
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello', 'world'], 'lo') == ['hello']
assert filter_by_substring(['hello', 'world'], 'goodbye') == []
```