```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Test cases
strings = ["abc", "bacd", "cde", "array", "text"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script provides a function called **filter_by_substring** that filters a list of strings based on a given substring.  It takes strings and substring as arguments, and returns a new list containing only the strings that contain the given substring.