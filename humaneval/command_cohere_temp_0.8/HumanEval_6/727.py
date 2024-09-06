```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        closed_brackets = []
        stack = []
        for c in segment:
            if c == '(':
                open_brackets.append(len(stack))
                stack.append(c)
            elif c == ')':
                closed_brackets.append(len(stack))
                stack.pop()
        result.append(max(open_brackets) + max(closed_brackets))
    return result
```