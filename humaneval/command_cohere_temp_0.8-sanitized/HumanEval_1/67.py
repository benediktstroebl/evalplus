from typing import List
import re
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    """
    closed_groups = []
    depth = 0
    for i in range(len(paren_string)-1, -1, -1):
        if paren_string[i] == '(':
            depth += 1
        elif paren_string[i] == ')':
            depth -= 1
            if depth == 0:
                closed_groups.append(paren_string[::-1][i+1:i-depth])
    return closed_groups