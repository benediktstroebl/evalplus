```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char != ' ']

# Test cases
tests = [
    "abc",
    "hello world",
    "0123456",
    "A",
    "123abc",
    "##!"
]

for test_case in tests:
    assert all_prefixes(test_case) == test_case.
```