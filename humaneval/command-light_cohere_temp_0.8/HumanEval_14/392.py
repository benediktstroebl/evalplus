```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [str for str in string if str != '']

# Test cases
test_data = [
    'abc',
    '',
    '123',
    'abc123',
]

test_cases = [
    ("All prefixes should be empty string"),
    (test_data[0], "all prefixes should be 'abc'"),
    (test_data[1], "all prefixes should be ''"),
    (test_data[2], "all prefixes should be '123'"),
    (test_data[3], "all prefixes should be 'abc123'"),
]

test_function = all_prefixes

for test, expected in test_cases:
    actual = test_function(test)
    assert actual == expected, f"Test case: {test} failed with expected: {expected}, actual: {actual}"
```