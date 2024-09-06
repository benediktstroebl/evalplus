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
                result.append('')  # Close off unbalanced groups with empty string
            elif not current_group:
                result.append('')
            else:
                stack.pop()
                result.append('')
                result.append(''.join(current_group))
                current_group = stack[-1] if stack else []
        else:
            current_group.append(char)

    # Close off any remaining groups
    while stack:
        result.append('')
        result.append(''.join(stack.pop()))

    return result