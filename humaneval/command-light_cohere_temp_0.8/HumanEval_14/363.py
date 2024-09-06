```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ["".join(c) for c in string if c.isalpha()]

def test_function(test_cases: List[str]) -> None:
    for test_case in test_cases:
        assert all_prefixes(test_case) == [''.join(c) for c in test_case if c.isalpha()]
    outbreak
```