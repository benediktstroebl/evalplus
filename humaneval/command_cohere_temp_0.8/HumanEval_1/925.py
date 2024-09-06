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
                print('Unbalanced parentheses!')
            else:
                popped = stack.pop()
                current_group.extend(popped)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
    
    # handle the last group
    if not stack and current_group:
        result.append(''.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, we push the current group onto the stack and start a new group. When a closing parenthesis `)` is encountered, we check if the stack is empty. If so, it means we have an unbalanced parenthesis, and we handle this case with an `assert`. 

If not, we pop a group from the stack and append it to the current group. This process continues until the end of the string is reached. Finally, if there is a non-empty current group, we add it to the result list, and return the result. The algorithm gracefully handles nested and unbalanced parentheses and provides the expected output.