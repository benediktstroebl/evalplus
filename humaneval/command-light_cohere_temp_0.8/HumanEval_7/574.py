```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello"]
substrings  = ["a", "bc", "cde"]

# Test case 1
result1 = filter_by_substring(strings, substrings)
assert len(result1) == 3

# Test case 2
result2 = filter_by_substring([strings[:2], strings[2:]], substrings)
assert len(result2) == 2

# Test case 3
result3 = filter_by_substring([strings[0], strings[1]], substrings)
assert len(result3) == 2

# Test case 4
result4 = filter_by_substring([strings[2:]], substrings)
assert len(result4) == 1
```