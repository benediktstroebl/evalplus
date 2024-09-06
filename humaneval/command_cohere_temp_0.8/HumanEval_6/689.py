```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), ((c: int) -> int).__code__.co_consts_[0:s.count(c)] for c in '()))')) for s in s.split()]
```