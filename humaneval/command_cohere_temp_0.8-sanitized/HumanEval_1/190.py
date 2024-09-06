from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    separate_groups = []
    open_parentheses = 0

    for char in paren_string:
        if char == '(':
            open_parentheses += 1
        elif char == ')':
            open_parentheses -= 1
        if open_parentheses < 0:
            raise ValueError("Invalid input. Unmatched parentheses.")
        if open_parentheses == 0:
            if not stack[-1]:
                stack.pop()
            else:
                separate_groups.append(stack.pop())
    return separate_groups