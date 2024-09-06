```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain the substring."""
    return [string for string in strings if substring in string]

# Test code
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
``` 
This Python script defines a function called **filter_by_substring** that filters a list of strings and returns a new list containing only the strings that contain a given substring. It uses the the in a "for" loop and returns a new list containing only the strings that contain the given substring.