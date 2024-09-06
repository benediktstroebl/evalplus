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
                tmp_group = stack.pop()
                current_group.extend(tmp_group)
                if not stack:
                    result.append(('').join(current_group))
                current_group = tmp_group
        else:
            current_group.append(char)
    
    return result