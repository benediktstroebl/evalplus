```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    return [max(i // 2 for i in reversed(sum(map(lambda x: list(zip(x, x[1:])), 
                iterables_of_pairs(s, '()))')))]

def iterables_of_pairs(s: str, op) -> List:
    result, curr = [], []
    for char in s:
        if char == op[0]:
            curr.append(char)
        elif char == op[1]:
            if curr:
                result.append(curr)
                curr = []
        else:
            curr.append(char)
    if curr:
        result.append(curr)
    return result
```