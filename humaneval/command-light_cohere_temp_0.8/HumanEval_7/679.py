```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Expected output: ['abc', 'bacd', 'array']
result = filter_by_substring(strings, substring)
print(result)

strings = ["a", "bc", "cde"]
substring = "cd"

# Expected output: ['cde"]
result = filter_by_substring(strings, substring)
print(result)
```
The function `filter_by_substring` takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The test cases demonstrate how the the expected behavior of the function for different input scenarios.