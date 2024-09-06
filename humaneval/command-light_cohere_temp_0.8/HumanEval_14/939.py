```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ' and char != '\n']

# Test the function with various inputs
tests = [
    ('',),
    ('a',),
    ('ab',),
    ('abc',),
    ('abcde'),
    (' ABC123 '),
    (' bar ',)
  ]

for test_case in tests:
    assert all_prefixes(test_case) == test_case
```