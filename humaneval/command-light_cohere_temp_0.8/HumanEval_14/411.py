```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return ['a' + c for c in string.a + 'bc']
```

def test_prefixes():
    assert all_prefixes('abc') == ['a', 'ab', 'abc'], "String not divided into prefixes correctly"

test_prefixes()
```