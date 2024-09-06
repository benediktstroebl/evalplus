from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            top_group = stack.pop()
            if not top_group:
                result.append(current_group)
            else:
                current_group = top_group + current_group
        else:
            current_group += char

    return result
input_string = '( ) (( )) (( )( ))'
result = separate_paren_groups(input_string)