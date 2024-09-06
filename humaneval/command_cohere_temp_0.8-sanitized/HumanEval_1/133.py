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
                print('Unexpected closing parenthesis')
                continue
            current_group.append(char)
            if not stack[-1]:
                result.append(')'.join(current_group))
                stack.pop()
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    if stack:
        print('Unclosed parentheses')
        
    return result