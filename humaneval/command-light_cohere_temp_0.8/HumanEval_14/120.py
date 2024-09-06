```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c != '' and c notstartswith(' ')]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("abcde", ["abcde"]),
    ("abcdefgh", ["abcdef", "acdefgh"]),
    (" ", []),
    ("a", ["a"]),
    ("aa", ["a", "aa"]),
]

for test_str, expected_result in test_cases:
    actual_result = all_prefixes(test_str)
    assert actual_result == expected_result, f" mismatch: {test_str} vs {expected_result}"
```
This Python script defines a function `all_prefixes` that returns a list of prefixes from a given string. It also provides a detailed set of test cases to check the function correctness, using the `typing` module for type hints.