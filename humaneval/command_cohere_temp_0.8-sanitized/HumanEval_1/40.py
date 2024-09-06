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
                print('Unbalanced parentheses!')
            else:
                popped_group = stack.pop()
                current_group.extend(popped_group)
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result