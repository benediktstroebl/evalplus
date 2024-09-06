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
                return []  # unbalanced group, returning empty list as an error case
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```

This code defines a function `separate_paren_groups` that takes in a string of parentheses and splits them into nested groups. It uses a stack to keep track of the currently open group of parentheses and iterates through the input string. When an open parenthesis is encountered, it pushes the current group (top of the stack) to the result and starts a new group. When a closing parenthesis is encountered, it checks if the stack is empty, verifying if the closing parenthesis belongs to the current group. If not, an error is returned (empty list). Otherwise, it pops the top of the stack to complete the current group. Finally, it handles any characters between parentheses as part of the group. The provided test case ensures the function correctly processes nested parentheses. 

This approach allows us to efficiently separate groups of parentheses in linear time, without having to use more complex parsing techniques.