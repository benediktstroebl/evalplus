```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.replace(' ', '').replace(')', ')(')) for _ in range(2)]):
        count = 1
        depth = 0
        while opening != closing:
            if opening == ')':
                count += 1
            if closing == '(':
                count -= 1
            if count > 0:
                depth += 1
            opening = closing
            closing = next(closing)
        result.append(depth)
    return result
```

The logic is straightforward:
1. We iterate over all pairs of parentheses in the string.
2. For each opening parenthesis, we count how many closing parentheses we need to get to until we are balanced.
3. The result is the depth of the recursion when we where balanced.