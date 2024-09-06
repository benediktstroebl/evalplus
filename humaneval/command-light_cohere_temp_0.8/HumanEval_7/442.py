```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test the function with sample inputs and known outputs
strings = ["abc", "bacd", "cde", "array", "abcd", "ab"]
substring = "a"
result = filter_by_substring(strings, substring)
assert len(result) == 4
```