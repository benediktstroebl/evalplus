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
                return []  # unbalanced group, returning empty list
            current_group += char
            if not stack[-1]:  # if the top of the stack is empty
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char
    
    return stack + [current_group]