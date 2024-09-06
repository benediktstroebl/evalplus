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
                print(f"Unmatched '{char}' in '{paren_string}'")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Unmatched '(' in '{paren_string}'")
        return []
    
    result.append("".join(current_group))
    
    return result