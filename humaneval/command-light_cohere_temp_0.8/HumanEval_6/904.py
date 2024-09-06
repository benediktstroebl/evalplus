```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                stack.pop()
            [if stack and not, char == ')':
                output.append(stack.pop()
               [else:
                    stack.push(0)
                else:
                        stack.append(1)
                    if char == ')' and not stack or len(stack) == 1:
                            output.append(stack.pop())
               return output
```