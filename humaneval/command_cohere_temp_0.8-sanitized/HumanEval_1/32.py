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
                result.append('')
            elif len(current_group) == 0:
                result.append('')
            else:
                prev_group = stack.pop()
                current_group.append(prev_group)
                if not stack:
                    result.append(''.join(current_group))
                else:
                    stack[-1].append(prev_group)
            current_group = []
        else:
            current_group.append(char)
    
    return result