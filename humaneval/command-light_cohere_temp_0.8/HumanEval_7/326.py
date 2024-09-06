```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Tests
strings = ["abc", "bacd", "cde", "array", "text"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters a list of strings and returns only those that contain a given substring.  The `typing` is used to type the function parameters, and the function performs the filtering operation. The code then tests the to make sure that the function behaves as expected.