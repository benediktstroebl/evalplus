```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(char) for char in string if char.isalpha()]
in string

def test_all_prefixes():
    assert all_prefixes("abc") == ['a', 'ab', 'abc']
    assert all_prefixes("").return longest() == ''
    assert all_prefixes("fps") == []
    assert all_prefixes("123") == ['1', '23']
    assert all_prefixes("!".join('.')) == []
```