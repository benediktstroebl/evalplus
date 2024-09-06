from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    open_braces = '([{'
    close_braces = ')]}'

    paren_groups = []
    stack = []

    for char in paren_string:
        if char in open_braces:
            stack.append(char)
        elif char in close_braces and stack:
            opening_brace = open_braces.index(stack.pop())
            group = ''.join(stack) + opening_brace + char + closing_brace
            paren_groups.append(group)

    return paren_groups