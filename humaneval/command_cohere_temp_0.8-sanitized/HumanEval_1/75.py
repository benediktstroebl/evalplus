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
                return []  # Unbalanced group, returning empty list as an error indication.
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append('')  # Empty group caused by unbalanced parentheses, adding as empty string
    
    return result