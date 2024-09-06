```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opened = False
    result = []
    for char in parentheses_string:
        if char == '(' and not opened:
            opened = True
            stack.append(1)
        elif char == ')' and opened:
            opened = False
            stack.pop()
       
            elif char == ')' and opened:
                result.append(stack.pop()
       
    other
        for x in range(len(stack)-1,-1)):
                    if stack[x] == 1:
                        stack[x] = 3
                    else:
                        stack[x] = 2
        return result
```