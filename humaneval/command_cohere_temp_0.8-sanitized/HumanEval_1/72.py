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
                result.append(')')
            else:
                current_group.pop()
                if not current_group:
                    result.append(')')
                else:
                    stack.pop()
                    result.append(')(')
                current_group = stack[-1]
        else:
            current_group.append(char)

    # Add remaining characters
    result.extend(current_group)
    return result