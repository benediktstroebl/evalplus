```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(c) for c in string if c != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    'abc123',
    'foo bar',
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    print(f'Expected: {['.join(c) for c in test_case], }, Actual: {})
    print(f[[c for c in actual_prefixes]])
```