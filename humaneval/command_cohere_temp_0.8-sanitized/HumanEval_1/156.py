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
                print('WRONG')
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)
            
    result.append(''.join(current_group))
    
    if not stack:
        return result
    else:
        print('WRONG')
        return []