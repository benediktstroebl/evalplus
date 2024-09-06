```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
            current_group = []
        else:
            current_group.append(char)
    
    return result
```

The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. At that point, it checks if the current group is nested within another by checking if the stack is empty. If it isn't, that means a closing parenthesis without an opening one was encountered, indicating the end of a group, and the stack top is added to the current group. If the stack is empty, the current group is added to the results and becomes the new stack top. This process ensures that unbalanced or nested groups are handled correctly.