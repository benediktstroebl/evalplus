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
                print(f"Unmatched close parenthesis '{char}'")
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Unmatched open parenthesis '('")
        return None
    
    result.append(''.join(current_group))
    
    return result