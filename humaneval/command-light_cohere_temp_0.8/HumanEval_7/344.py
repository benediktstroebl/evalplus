```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substrings = ["a", "bc"]
result = filter_by_substring(strings, substrings)
print(result)  # ['abc', 'bacd', 'array']
```