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
                current_group = top_group + current_group
        else:
            current_group += char
    return result
```

The code uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the code checks if it matches the most recent opening parenthesis (top of the stack). If it does, the group is added to the result list and the stack is popped. If it doesn't, the group is added to the stack to handle nested groups. Finally, the script returns a list of the separated groups.