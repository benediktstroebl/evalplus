from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            if stack:
                current_group += ')'
                stack.pop()
            else:
                current_group += char
        else:
            current_group += char
    
    return stack + [current_group]