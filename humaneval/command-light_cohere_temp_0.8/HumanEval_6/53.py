```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                stack.pop()
            else:
                stack.append(stack.append(0))
            elif char == '(' and stack:
                stack[-1] = 3
            stack.append(1)
        elif char == ')':
                stack.pop()
                stack.append(0)
    return stack
```

This code defines a function parse_nested_parens that takes a string of nested parentheses as input and returns a list of integers representing the depth of each nesting level. The function uses a approach similar to a stack to keep track of opening parentheses.