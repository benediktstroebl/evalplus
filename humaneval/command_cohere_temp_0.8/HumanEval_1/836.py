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
                return [top_group]
            if top_group == "":
                current_group = ""
            else:
                stack.append(top_group)
                current_group = ""
    return stack if stack else [current_group]
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the most recently added string to the stack is taken as the name of the group and removed from the stack and subsequently added to the result list only if the current group is empty. This ensures that nested groups are correctly handled. If the stack is empty, the current group is added. The result list is returned after processing all characters in the string. This approach avoids explicit nested iteration and ensures the correctness of group separation.