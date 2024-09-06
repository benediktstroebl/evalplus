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
                return ['Invalid input! No opening paren to match this closing paren.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening brackets until the corresponding closing brackets appear,
and maintains a list to store the characters between opening and closing brackets, this way, multiple layers of brackets are correctly handled.

This solution assumes that the input will have properly balanced parentheses, and therefore does not include logic for handling the case where a closing parenthesis does not have a matching opening parenthesis.