```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# Function call and assertion
assert filter_by_substring(strings, substring), ["Error: Failed to filter"]
```
This code provides a function `filter_by_substring` that filters an input list of strings based on a given substring. It uses the distinct and concise syntax for assigning and asserting test cases, which enhances readability and avoids potential errors.