from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            top_of_stack = stack.pop()
            if top_of_stack == "":
                current_group = ""
            elif top_of_stack != current_group:
                print("Warning: Nested or unbalanced parentheses!")
            current_group = ""
    
    return stack