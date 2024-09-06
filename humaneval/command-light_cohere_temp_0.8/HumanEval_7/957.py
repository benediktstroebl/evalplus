```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. It then passes tests and demonstrates the list of strings and the target substring, and the output is displayed, showing the filtered strings that contain the substring.