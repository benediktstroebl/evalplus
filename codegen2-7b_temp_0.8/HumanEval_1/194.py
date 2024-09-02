from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[str] = []
    paren_string = paren_string.replace(" ", "")
    for c in paren_string:
        if c == '(':
            stack.append('(')
        elif c == ')':
            if len(stack) == 0:
                return []
            elif stack.pop()!= '(':
                return []
    if len(stack) == 0:
        return paren_string.split(",")
    return
