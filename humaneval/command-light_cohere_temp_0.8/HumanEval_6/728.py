```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack: List[int] = []
    result: List[int] = []
    for char in parenthes_str:
        if char == '(':
            stack.append(0)
        else:
            stack.pop()
       if is [0]
        stack.append(char)
    if len(stack) == 0:
            result.append(len(stack))
        elif len(stack) == 1 and stack[0] == 0:
            result.append(1)
        elif len(stack) > 1:
            for level in range(2, len(stack) - 1, -1):
                if stack[level] == '()':
                    result.append(3)
                elif stack[level] == '(' or stack[level] == ')':
                    result.append(1)
                else:
                    result.append(0)
            else:
                result.append(2)
    return result
    ```