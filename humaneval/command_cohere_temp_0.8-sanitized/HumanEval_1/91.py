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
                print('Warning: Extra closing parenthesis.')
            else:
                current_group.append(char)
                stack.pop()
                if not stack:
                    result.append(''.join(current_group))
                    current_group = stack[-1]
                else:
                    current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result