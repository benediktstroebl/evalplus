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
                print('Unmatched close parenthesis')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The code uses a stack to keep track of opening parentheses '(' and correctly close parentheses ')' to separate the groups of parentheses. Each '(' pushed to the stack is associated with a new group that is saved in the `current_group` list. The code also handles the case when the input string ends with an unmatched close parenthesis ')' by checking if the stack is empty when trying to pop it.