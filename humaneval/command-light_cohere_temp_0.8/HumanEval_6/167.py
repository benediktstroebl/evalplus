```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    result = []
    for c in parenthes_str:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] == 1:
                result.append(stack.pop()
           
            then stack
        else:
                stack.append(0)
    else:
                stack.append(stack.pop() + 0)
    maximum nesting.
```