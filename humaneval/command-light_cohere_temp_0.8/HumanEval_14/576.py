```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(x) for x in string if x != '']

# Test the function with various strings
test_cases = [
    "abc",
    "",
    "123",
    "abc123",
    "foo bar faz",
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    expected_prefixes = ['.a' for _ in test_str if _ != '']
    assert actual_prefixes == expected_prefixes
```