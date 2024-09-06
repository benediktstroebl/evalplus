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
            if stack:
                current_group = stack.pop()
            else:
                result.append(')')
        else:
            current_group.append(char)
    
    if stack:
        # add remaining open parentheses
        while stack:
            current_group.append(')')
            stack.pop()
        result.append('(' + ''.join(current_group))
    else:
        result.append('')
    
    return result