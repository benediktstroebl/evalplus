```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(char for char in string if char != ' ') + '' for _ in range(10)]
def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```