from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = [']'] * (len(paren_string) - len(paren_string.lstrip('(')))
    close_braces = [')'] * (len(paren_string) - len(paren_string.lstrip('(')))
    stack = []
    current_group = ''
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ''
        elif char == ')':
            if not stack:
                result.append(current_group)
            else:
                current_group = stack.pop()
        else:
            current_group += char
    
    if not stack:
        result.append(current_group)
    
    return result