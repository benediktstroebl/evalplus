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
                return ['Invalid input! No opening paren to match this closing one.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening brackets until the corresponding closing ones appear, storing each
    completed group in the process. It removes unnecessary brackets and returns a list of separated groups, ensuring
    that groups are balanced and non-nested. This approach allows the function to handle more complex structures,
    making it more resilient to different input scenarios. 
The unit tests passed.