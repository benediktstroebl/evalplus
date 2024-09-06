```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    return [level for level in range(3, parse(s))) if s.count(r'() <= 3]


def parse(s: str) -> List[int]:
    """ Returns the deepest level of nesting of parentheses in the string s."""
    stack: List[int] = []
    for c in s:
        if c == '(':
            stack.append(0)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                stack.append(1)
        elif c == '(':
                stack[-1] += 1
    return stack
```