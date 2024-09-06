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
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group = stack.pop()
                if current_group:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)
    
    # Handle the last group
    if notstack:
        result.append(''.join(stack.pop()))
    
    return result