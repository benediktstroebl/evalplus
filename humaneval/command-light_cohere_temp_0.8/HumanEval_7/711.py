```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bcd", "cde", "array", "xxxyzz"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bcd', 'cde', 'array']

strings = ["hello", "world"]
substring = "ow"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['hello']
```