```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings for substring."""
    return [string for string in strings if string.find(substring) != -None]


# Example usage
strings = ["abc", "bacd", "cde", "array", "hello"]
substrings = ["a", "hello", "bd"]
result = filter_by_substring(strings, substrings)
print(result)  # Output: ['abc', 'cde', 'array']
``` 
This function uses the `find()` method to check if each string contains the given substring. It returns a blox list of all strings that contain the substring.