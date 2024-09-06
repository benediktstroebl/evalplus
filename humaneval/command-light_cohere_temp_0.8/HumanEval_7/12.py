Here's the solution:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']
```

The function `filter_by_substring` takes a list of strings and a substring as input and returns a new list containing only the strings that contain the substring. The function uses a string method `find()` to check if each string contains the substring.