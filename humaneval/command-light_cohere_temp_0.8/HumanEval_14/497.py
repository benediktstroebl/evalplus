```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char.isalpha()]

def test_all_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('abcd') == ['a', 'ab', 'acd']
    assert all_prefixes('') == []
test_all_prefixes()
```