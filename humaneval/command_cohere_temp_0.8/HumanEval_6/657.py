```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for interval in s.split(' '):
        level = 0
        unbalanced = 0
        for char in interval:
            if char == '(':
                level += 1
                unbalanced += 1
            elif char == ')':
                if unbalanced > 0:
                    level += 1
                    unbalanced -= 1
                else:
                    result.append(level)
                    unbalanced = 0
            elif char == ' ':
                if unbalanced > 0:
                    result.append(level)
                    unbalanced = 0
            else:
                unbalanced += 1
        if unbalanced > 0:
            result.append(level)
            unbalanced = 0
    return result
```

The approach involves iterating over each interval (string between two spaces) and tracking the level of nesting using `level` variable. `unbalanced` variable keeps track of unbalance opening parentheses. Whenever we encounter a closing parenthesis, we adjust the level and unbalanced variable accordingly. When string segment ends, we check unbalanced variable. If it's greater than 0, this means some opening parentheses never got closed, hence the level is incremented by unbalanced times.

This way, the result contains the deepest level of nesting for each interval.