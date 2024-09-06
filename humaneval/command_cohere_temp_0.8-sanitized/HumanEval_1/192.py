import re
from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    stack = []
    patterns = re.findall(r'(\([^()]*\))', paren_string)
    for pattern in patterns:
        if pattern[0] == '(':
            stack.append(pattern)
        else:
            stack.pop()
            if not stack or stack[-1][0] != '(':
                result.append(''.join(stack))
                stack = []
    if stack:
        result.append(''.join(stack))
    return result
paren_string = '( ) (( )) (( )( ))'