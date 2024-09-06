```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string if x != '']

# Test cases
test_cases = [
    'abc',
    'ABCDEFGHIJKLMNOPQRSTUVZW',
    'abc123',
    'hello world',
    '',
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    expected_prefixes = ['', 'ab', 'abc', 'abc123', 'hello']
    assert actual_prefixes == expected_prefixes
```