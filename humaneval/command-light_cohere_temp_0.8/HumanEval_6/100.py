```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for c in parent_string:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if stack:
                stack.pop()
                if stack[-1] == 1:
                    output.append(stack.pop()
                while all '('('))
                output.append(1)
                stack = []
        else:
            stack.append(0)
    output.append(stack[-1])
    return output
```