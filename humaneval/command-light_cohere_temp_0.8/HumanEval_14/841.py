```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.str.split() if len(string) >= 2]

# Unit tests
def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

test_all_prefixes()
```