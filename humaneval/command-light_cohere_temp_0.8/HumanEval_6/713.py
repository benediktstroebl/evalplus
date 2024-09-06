```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    for c in s:
        if c == '(': stack.append(1)
        elif c == ')':
            if not stack or stack[-1] != 1:
                raise ValueError("Unexpected character!")
            stack.pop()