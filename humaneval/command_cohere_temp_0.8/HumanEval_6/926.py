```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), counter(c for c in s if c == '(')))))]

def counter(char: str) -> int:
    count = 0
    while char in s:
        s = s.replace(char, '')
        count += 1
    return count
```