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
            top_group = stack.pop()
            if top_group == current_group:
                current_group = top_group
            else:
                current_group = ""
    return stack