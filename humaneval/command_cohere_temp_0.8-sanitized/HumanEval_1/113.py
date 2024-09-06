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
                stack.pop()
                current_group.append(')')
        else:
            current_group.append(char)

    # Add the last group
    if current_group:
        result.append(''.join(current_group))

    # Add any remaining open parentheses
    while stack:
        result.append(')')
        stack.pop()

    return result