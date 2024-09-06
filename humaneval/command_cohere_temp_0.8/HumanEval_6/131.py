```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        stack = []
        for c in token:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

This script includes the function `parse_nested_parens()` which takes a string `s` as input and returns a list of deepest levels of nesting of parentheses in each group. The function uses a stack to track the nesting level for each group.