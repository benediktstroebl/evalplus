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
                return []  # Unbalanced parenthesis, returning empty list as an error indication.
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Adding the last group to the list
    result.extend(stack)
    result.append(current_group)

    return result