```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        delta = 1
        while opening:
            if opening.count('(') == closing.count(')'):
                depth += 1
            else:
                break
            opening = opening.replace('(', '').replace(')', '')
            closing = closing.replace('(', '').replace(')', '')
        result.append(depth)
    return result
```

The algorithm works by iterating through each pair of parentheses and incrementing a counter if the number of opening and closing parentheses is equal. If it isn't equal, the loop is terminated and the counter is appended to the result list.