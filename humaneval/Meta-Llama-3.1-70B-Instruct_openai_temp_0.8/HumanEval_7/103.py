```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    Filter an input list of strings only for ones that contain given substring.

    Args:
        strings (List[str]): A list of strings to be filtered.
        substring (str): A substring that the strings should contain.

    Returns:
        List[str]: A list of strings that contain the given substring.
    """
    return [s for s in strings if substring in s]


# Test cases
print(filter_by_substring([], 'a'))  # Expected output: []
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))  # Expected output: ['abc', 'bacd', 'array']
print(filter_by_substring(['hello', 'world', 'python','coding'], 'o'))  # Expected output: ['hello', 'world', 'coding']
print(filter_by_substring(['apple', 'banana', 'orange', 'grape'], 'an'))  # Expected output: ['banana', 'orange', 'grape']
```