```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), Counter(c for c in s.split(' ') if c == '())))))) for _ in range(len(s.split(' ')))]
```