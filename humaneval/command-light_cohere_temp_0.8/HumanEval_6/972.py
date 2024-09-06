```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opened = False
    in_string = False
    output: List[int] = []
    for char in parentheses_string:
        if char == '(':
            if opened:
                stack.append(1)
            opened = True
        else:
            stack.append(None)
            opened = False
            in_string = False
        elif char == ')':
            if not_string:
                stack.append(1)
            elif opened:
                stack.append(3)
                opened = False
            else:
                stack.append(None)
                in_string = False
        elif char in ' \t':
            if opened or in_string:
                stack.append(None)
            in_string = False
        else:
            in_string = True
        output.append(stack.pop())
   
   
    list(map(int, stack)))
    return output
```