```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join()[i::1] for i, char in enumerate(string, 1)]

# Test the function with various strings
test_cases = [
    ("abc",), ("a",), ("a", "bc"), ("ab", "bc"),
    ("",), ("123",), ("abcd",), ("abcde",)
]

for test_str, expected_result in test_cases:
    actual_result = all_prefixes(test_str)
    assert actual_result == expected_result, f"For '{test_str}', expected [{expected_result}], got [{actual_result}]"
```