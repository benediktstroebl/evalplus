```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [''.join([ch for ch in string if ch not in 'abcdef']) for _ in range(10)]
for x in range(10):
    assert all_prefixes(''.join(x)) == [''.join([x+1])]
```