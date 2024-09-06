```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join(char) for char in string if char != ''] + [string]
test_cases = [
    "abc",
    "123",
    "aa",
    "",
    "a",
    "##",
]

for case in test_cases:
    assert all_prefixes(case) == case.
```