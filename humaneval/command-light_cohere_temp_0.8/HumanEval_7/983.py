```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
#unit tests
strings = ["abc", "bacd", "cde", "array", "apple", "car"]
substring = "a"
print(filter_by_substring(strings, substring))  # ['abc', 'bacd', "array"]
```