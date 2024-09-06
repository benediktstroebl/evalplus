from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = [0]
    close_braces = [0]
    output = []
    stack = []
    
    for char in paren_string:
        if char == '(':
            open_braces[0] += 1
        elif char == ')':
            close_braces[0] += 1
        else:
            continue
        
        if open_braces[0] == close_braces[0]:
            if open_braces[0] > 0:
                stack.append(")" * open_braces[0])
                open_braces[0] = 0
                close_braces[0] = 0
        elif open_braces[0] > close_braces[0]:
            open_braces[0] -= 1
        else:
            close_braces[0] -= 1
    
    while stack:
        output.append("(" + stack.pop() + ")")
    
    return output
paren_string = "( ) (( )) (( )( ))"