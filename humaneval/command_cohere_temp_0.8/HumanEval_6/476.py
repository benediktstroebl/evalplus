```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for tok in s.split():
        level = 0
        stack = []
        for c in tok:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The code uses a stack to track the nesting level of parentheses. When a left parenthesis `(` is encountered, it is appended to the stack, increasing the level by 1. Conversely, when a right parenthesis `)` is encountered, it is popped from the stack, reducing the level by 1. The function splits the input string into individual tokens (groups of parentheses) and processes each token separately to determine its deepest level of nesting. The resulting list of nesting levels corresponds to the input order of the groups.