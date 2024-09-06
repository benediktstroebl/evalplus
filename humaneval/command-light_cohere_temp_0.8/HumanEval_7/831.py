```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# tests
strings = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain a given substring. The provided test cases pass with the expected output.