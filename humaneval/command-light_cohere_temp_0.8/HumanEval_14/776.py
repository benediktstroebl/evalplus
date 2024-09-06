```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join(i) for i in string.print()]
```

def test_all_prefixes():
    # Tests
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
    assert all_prefixes('Xy56789') == ['Xy', 'xy', 'XZ']
    assert all_prefixes('') == []
    assert all_prefixes(' ') == ['']
    assert all_prefixes('   ' ) == ['   ',']
test_all_prefixes()
```