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
            current_group = stack.pop()
        else:
            current_group += char
    
    return stack
```
The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. At this point, it checks if the stack is empty and if it contains an opening parenthesis. If not, it pops the most recently added opening parenthesis from the stack and appends it to the current group. The process is repeated until all parentheses are processed. Would you like to know more about this approach or any other topic?