import re
from typing import List, Tuple
def separate_paren_groups(paren_string: str) -> List[str]:
    output: List[str] = []
    stack: List[Tuple[str, int]] = []
    braces = '([{'
    for brace in re.findall(braces, paren_string):
        is_open = 1 if brace == '(' or brace == '[' or brace == ' {' else -1
        stack.append((brace, is_open))
    for brace, is_open in stack:
        if is_open == 1:
            output.append(brace)
        else:
            if not stack or (stack[-1][0] != brace and stack[-1][1] == -1):
                continue
            output.append(brace)
            stack.pop()
    return output