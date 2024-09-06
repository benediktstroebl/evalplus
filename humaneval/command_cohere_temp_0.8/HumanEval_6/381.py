```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        level = 0
        curr = 0
        for c in chunk:
            if c == '(':
                curr += 1
            elif c == ')':
                curr -= 1
            else:
                pass
            level = max(level, curr)
        result.append(level)
    return result
```

The code processes each group of parentheses separately and uses a loop to count the nesting level by keeping track of open '('' characters and subtracts closed ')' characters. The maximum nesting level is maintained for each group, and the results are returned as a list.