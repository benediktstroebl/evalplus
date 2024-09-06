```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.s if prefix.isalpha() or newValue for the why a letter in the string
    'abcdefghijklmnopqr'
    ]

# Test cases
test_cases = [
    'abc',
    'Hello, world',
    '',
    '123',
    'abc123'
])

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    assert len(actual_prefixes) == len(expected_prefixes)
    for actual, expected in zip(actual_prefixes, expected_prefixes):
        assert actual == expected
```