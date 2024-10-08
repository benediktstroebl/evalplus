```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), ((c, n) for n, c in zip(s.split(), s.split())))))] for _ in s.split()]
```