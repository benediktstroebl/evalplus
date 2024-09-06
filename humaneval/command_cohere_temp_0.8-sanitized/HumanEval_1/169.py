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
                result.append('')  # If we have an extra closing brace, consider it a separate group
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Handle any remaining open parentheses
    while stack:
        temp_group = stack.pop()
        current_group.extend(temp_group)
        result.append(''.join(current_group))
        current_group = []

    return result