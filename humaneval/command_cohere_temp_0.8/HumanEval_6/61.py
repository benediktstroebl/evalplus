```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), ((c, n) for c, n in zip(s.split(), itertools.count(0)) + [('', 0)] * len(s)))))]
```