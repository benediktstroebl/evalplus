from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list
            current_group += char
            if not stack[-1]:  # If the top of the stack is empty, pop it
                stack.pop()
            if not current_group:  # If the current group is empty, pop the stack
                stack.pop()
    
    return stack if not current_group else stack + [current_group]