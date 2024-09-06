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
                print(f"Unmatched right parenthesis '{char}'.")
        
        # Ensure current group is appended to stack (to account for unbalanced groups)
        if not stack and current_group:
            stack.append(current_group)
            current_group = ""

    return stack
```
This approach uses a stack to keep track of nested groups of parentheses. When we encounter a left parenthesis, we append the currently collected group to the stack, and start a new group. When we encounter a right parenthesis, we check if the stack is empty. If so, there's an unmatched right parenthesis. Otherwise, we pop the top group from the stack, and append the current group. This handles both balanced and unbalanced groups, with the assumption that the input contains only parentheses and no other characters.