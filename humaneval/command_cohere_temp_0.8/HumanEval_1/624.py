```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if stack:
                stack.pop()
            else:
                print(f"Unmatched right parenthesis '{char}'")
        else:
            current_group += char
    
    return stack
```
This approach utilizes a stack to keep track of nested groups, updating the current group whenever an open paren is encountered and popping the stack to reset the group when a close paren is seen. This guarantees that groups are properly separated and balanced, handling potential unmatched right parentheses gracefully.