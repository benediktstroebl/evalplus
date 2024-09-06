```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), counter(c for c in s if c == '(')))))]

def counter(char: str) -> List[int]:
    count = len(char) * [0]
    count_idx = count.copy()
    for i, c in enumerate(char):
        count[c] += 1
        count_idx[c] = i
    return count, count_idx
```