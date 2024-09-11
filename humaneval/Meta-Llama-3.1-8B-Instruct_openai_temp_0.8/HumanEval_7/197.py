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

    Examples:
        >>> filter_by_substring([], 'a')
        []
        >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
        ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]

# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
assert filter_by_substring(['hello', 'world'], 'o') == ['hello', 'world']
assert filter_by_substring(['apple', 'banana'], 'orange') == []
```

This script uses a list comprehension to filter the input list of strings based on whether they contain the given substring. The unit tests at the end ensure the function behaves as expected for various input cases.