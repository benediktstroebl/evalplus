```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
# Unit tests
strings = ["abc", "bacd", "cde", "array", "test"]
substring = "a"

test_filter = [
    assert filter_by_substring(strings, substring) == ['abc', "bacd", "array"],
    assert filter_by_substring(strings, "td") == []
]
```
The provided code has a function `filter_by_substring` that filters a list of strings based on a given substring. The unit tests below verify that function's correctness: