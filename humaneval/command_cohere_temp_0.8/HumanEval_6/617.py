```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brackets = []
        close_brackets = []
        stack = []
        for c in segment:
            if c == '(':
                open_brackets.append(len(stack))
                stack.append(c)
            elif c == ')':
                close_brackets.append(len(stack))
                stack.pop()
        result.append(max(open_brackets)[0] + max(close_brackets)[0] + 1)
    return result
```