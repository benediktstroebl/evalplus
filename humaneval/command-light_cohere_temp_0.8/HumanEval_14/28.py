```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in range(1, len(string)+1)]

# Test cases
test_cases = [
    ("abc", ["a", "ab", "abc"]),
    ("hello world!", ["hello", "hw", "world"]),
    ("àèêöö", ["à", "é", "ê", "ö"]),
    # long strings for longer test
    ("abc123123", ["abc", "abcs", "abc123"]),
]

for test_case, expected_result in test_cases:
    actual_result = all_prefixes(test_case)
    assert actual_result == expected_result, f"Unexpected result: {actual_result}, expected: {expected_result}"
``` 
This code defines a function all_prefixes that returns a list of all prefixes of a given string, ranging from shortest to longest. The function is then tested using several test cases to ensure its correctness.