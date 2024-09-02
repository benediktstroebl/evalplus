from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_braces: List[int] = []
    current_open_brace = None
    open_braces.append(-1)

    for i, c in enumerate(paren_string):
        if c == '(' or c == ')':
            if c == '(':
                current_open_brace = i
            elif c == ')' and current_open_brace > open_braces[-1]:
                open_braces.append(i)

    ret = []
    start = 0
    for i in range(len(open_braces)):
        end = open_braces[i]
        ret.append(paren_string[start:end + 1])
        start = end + 1
    return ret
    pass
