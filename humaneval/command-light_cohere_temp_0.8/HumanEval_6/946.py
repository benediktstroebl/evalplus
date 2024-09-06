```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[str] = []
    output: List[int] = []
    for ch in s:
        if ch == '(':
            stack.append('(')
       
        elif ch == ')':
            stack.append(')')
       
            else:
                stack.append(ch)
    if len(stack) == 0:
                    output.append(0)
                else:
                    last_level = int(stack.pop())
                    current_level = 1
                    while current_level < last_level:
                        stack.append(')')
                    else:
                        output.append(last_level + 1)
    return output
```