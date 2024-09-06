```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), counter(c for c in s if c == '(')))))]

def counter(letter):
    count = 0
    while letter in ['(', ')']:
        letter = next(input())
        count += 1
    return count
```