```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring that must be present in the strings.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [string for string in strings if substring in string]


# Test cases
assert filter_by_substring([], 'a') == []
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

# Additional test cases
assert filter_by_substring(['hello', 'world'], 'hello') == ['hello']
assert filter_by_substring(['hello', 'world'], 'goodbye') == []
assert filter_by_substring(['apple', 'banana', 'cherry'], 'an') == ['banana', 'cherry']
```

This script defines a function `filter_by_substring` that filters a list of strings to only include strings that contain a given substring. It then includes several test cases to demonstrate the function's behavior. The test cases cover various scenarios, including an empty list, a list with multiple matching strings, and a list with no matching strings.