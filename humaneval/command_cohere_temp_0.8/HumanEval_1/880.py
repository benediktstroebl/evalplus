```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            top_group = stack.pop()
            if not stack:
                result.append(top_group)
            else:
                stack[-1] += top_group
        else:
            current_group += char

    return result
```
The code uses a stack to keep track of nested parentheses groups. When encountering a left parenthesis, it saves the current group and starts a new one. When encountering a right parenthesis, it checks if the stack is empty. If it isn't, the top element is appended to the current group and the stack is popped. If the stack is empty, the current group is the last one, so it's appended to the result and the function returns. Ultimately, this process effectively separates the nested parentheses groups into a list, regardless of nesting levels or spacing.