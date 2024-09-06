```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            elif len(stack) == 1:
                output.append(stack.pop())
            else:
                    stack.append(int)
            else:
                stack.append(ord(char) - 1)
    return output
```