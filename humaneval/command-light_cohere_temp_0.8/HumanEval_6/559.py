```python
from typing import List
def parse_nested_parens(parenthes: str) -> List[int]:
    stack: List[int] = []
    output: List[int] = []

    for char in parenthes:
        if char == ')':
            if not empty():
                stack.append(len)
            empty = False
        elif char == '(':
            empty = True
        else:
            empty = False

        if char == '':
            stack.append(0)
        elif char == ')':
            stack.pop()
        count = stack.pop()
            levels = count // 2
            if levels == 0:
                output.append(count)
            else:
                output.add(count, levels)

    return output
```