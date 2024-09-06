```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(string[i:]) for i in range(0, len(string), 1)]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("123", ["123"]),
    ("", []),
    ("a", ["a"]),
    ("abcde", ["abc", "ade"]),
]

for test_str, expected_result in test_cases:
    actual_result = all_prefixes(test_str)
    assert actual_result == expected_result, f"Error in test case: {test_str} should have: {expected_result}, but got: {actual_result}"
```