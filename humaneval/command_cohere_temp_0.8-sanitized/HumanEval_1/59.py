from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    stack: List[str] = []
    current_group: str = ''
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ''
        elif char == ')':
            current_group += char
            if stack:
                stack.pop()
            else:
                print('Warning: Extra closing parenthesis.')
        else:
            current_group += char
    
    return stack