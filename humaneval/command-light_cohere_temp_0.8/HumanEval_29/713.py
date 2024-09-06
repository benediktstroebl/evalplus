```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Unit tests
strings = ["abc", "bcd", "cde", "a", "array", " narrative"]
prefix = "a"

test_strings = [
    "This is a ",
    "test string ",
    " pass",
    " good morning"
]

test_prefix = "p"

should = filter_by_prefix(strings, test_prefix)

print(should)
```