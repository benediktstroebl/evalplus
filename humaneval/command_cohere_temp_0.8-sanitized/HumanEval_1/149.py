from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    separate_groups = []
    stack = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                separate_groups.append('')
            else:
                separate_groups.append('')
    return separate_groups