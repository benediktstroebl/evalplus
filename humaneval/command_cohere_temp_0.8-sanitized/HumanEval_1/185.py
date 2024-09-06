from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    output = []
    current_group = ''

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                # Nested or unbalanced group, add it to the current group
                current_group += char
            else:
                # Properly closed group, add it to output
                output.append(current_group)
                current_group = ''
    output.append(current_group)
    
    return output