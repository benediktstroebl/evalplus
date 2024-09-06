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
                return []  # Unbalanced group, returning empty list as an indication of error
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle potential remaining characters
    while stack:
        current_group.extend(stack.pop())

    result.extend(current_group)
    return result