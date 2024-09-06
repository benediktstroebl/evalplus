from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    open_paren = 0
    for char in paren_string:
        if char == '(':
            open_paren += 1
        elif char == ')':
            open_paren -= 1
        elif open_paren == 0:
            stack.append(paren_string[open_paren-1:])
            open_paren = -1
        elif open_paren > 0:
            stack[-1] += '(' + paren_string[open_paren-1:].strip() + ') '
            open_paren -= 1
    if open_paren > 0:
        stack[-1] += '(' + paren_string[open_paren-1:].strip() + ') '
    return stack
