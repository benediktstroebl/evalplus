```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(). (i for i, char in enumerate(string)) for _ in range(1, len(string)) if char != "" and string[:i] == char]

# Test cases
test_cases = [
    "abc",
    "hello world",
    "   ",
    ""
]

for test_str in test_cases:
    actual_prefixes = all_prefixes(test_str)
    assert len(actual_prefixes) == len(test_prefixes)
    assert all_prefixes == test_prefixes
```