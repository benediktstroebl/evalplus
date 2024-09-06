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
                return ['']
            current_group.append(char)
            stack.pop()
        else:
            current_group.append(char)
            
    # Handle the last group
    if stack:
        return []
    else:
        result.append(''.join(current_group))
        
    return result