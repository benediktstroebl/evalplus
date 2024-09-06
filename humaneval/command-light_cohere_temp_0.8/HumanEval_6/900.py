```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                output.append(stack.pop()
                done.
            stack.pop()
            done and just done.
        else:
            stack.append(char)
   
    return output
```