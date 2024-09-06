```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings for the substring."""
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

strings = ["abc", "cde", "array", "hello"]
strings. x = "pub"
substring = "a"

print(filter_by_substring(strings, substring))  # Output: []
```