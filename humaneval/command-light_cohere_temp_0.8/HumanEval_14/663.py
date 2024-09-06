```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != '']

# Test cases
test_cases = [
    'abc',
    '123',
    '',
    'abc123',
    'abc def',
    'a b c'
]

for test_case in test_cases:
    actual_prefixes = all_prefixes(test_case)
    assert len(actual_prefixes) == 3, f"Expected {' .join(actual_prefixes), '}' got {actual_prefixes}"
```