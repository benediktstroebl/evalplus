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
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```
The code uses a stack to keep track of opening parentheses '('. When a closing parenthesis ')' is encountered, the stack is checked to see if it's empty (indicating an unbalanced parenthesis) or if it contains an opening parenthesis. If it does, the top element of the stack is appended to the current group, and the stack is popped to continue processing the current group. If the stack is empty, the code prints an error message indicating unbalanced parentheses. The resulting list of strings, representing the separate groups of parentheses, is finally returned.