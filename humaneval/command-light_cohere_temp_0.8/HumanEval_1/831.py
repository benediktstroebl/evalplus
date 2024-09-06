```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of parentheses into separate strings."""
    stack: List[str] = []
    result = []
    in_string = False
    for char in s:
        if char == ' ':
            if not in_string:
                in_string = True
                stack.append(char)
            else:
                stack.append(' ')
       
        if len(stack) == 0:
                result.append('(')
                in_string = False
                continue
        elif in_string:
            stack.append(char)
        else:
            in_string = False
            if char == ')':
                stack.pop()
                if stack:
                    result.append(''.append(stack.pop())
                if stack == []
                stack = []
    return result
```