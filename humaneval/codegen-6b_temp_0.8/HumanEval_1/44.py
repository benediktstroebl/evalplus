from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    separated = []
    scanned = []
    stack = []
    i = 0

    for char in paren_string:
        if char == ')':
            if len(stack) == 0:
                return None
            opened = stack[-1]
            stack.pop()
            if opened == '(':
                separated.append(''.join(scanned))
                scanned = []
            else:
                scanned.append(opened)
        elif char == '(':
            stack.append('(')
        elif char == ' ':
            pass
        else:
            scanned.append(char)

    if len(scanned) != 0:
        separated.append(''.join(scanned))

    return separated

