```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "att"]
substrings = ["a", "bd", "cde", "ar"]

test_filter = [
    assert filter_by_substring(strings, substrings) == ["abc", "bacd", "array"],
    assert filter_by_substring(strings, substrings[1:]) == [],
    assert filter_by_substring(strings, "x") == []
]

print("All tests passed!")
```