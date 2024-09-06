```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])),
        (subscript(s, i + 1, j + 1), subscript(s, i, j)) for j in range(len(s)) if i != j and s[i] == '(' and s[j] == ')'
    )))) for i in range(len(s))]

def subscript(s, i, j):
    return s[i:j + 1]
```