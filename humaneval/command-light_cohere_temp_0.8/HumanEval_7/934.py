```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
#Tests
strings = ["abc", "bacd", "cde", "array", "123", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters an input list of strings and returns a new list that includes only the strings that contain the given substring. The test section demonstrates the desired output and function behavior.