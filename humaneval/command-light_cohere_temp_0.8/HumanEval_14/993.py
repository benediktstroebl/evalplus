```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a' if c.isalpha() else c.isbeta() else c else c else '']: [str(c) for c in string]
def testcase():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']
```