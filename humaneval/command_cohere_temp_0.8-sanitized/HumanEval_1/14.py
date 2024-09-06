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
                result.append(')')
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)
            
    # Handle possible remaining open parentheses
    while stack:
        temp = stack.pop()
        current_group.extend(temp)
        
    # Close all groups and add to result
    for group in current_group:
        if group == '(':
            result.append('')
        else:
            result.append(')')
    result.extend(current_group)
        
    return result