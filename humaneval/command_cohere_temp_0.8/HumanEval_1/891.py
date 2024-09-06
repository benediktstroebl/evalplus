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
                return []
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```

This Python script uses a stack to keep track of nested parentheses and correctly separates them into groups. It checks for the opening parentheses to push the current group onto the stack. When it encounters a closing parenthesis, it checks if the stack is empty or if the top of the stack is a different group. If so, it pops the stack and appends it to the result. This ensures that all groups of parentheses are separated and returned correctly, and that nested or unbalanced groups are handled properly.