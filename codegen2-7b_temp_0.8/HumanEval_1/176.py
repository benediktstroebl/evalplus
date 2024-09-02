from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens = []
    in_paren = False
    paren_string = paren_string.strip()
    for c in paren_string:
        if c == '(':
            in_paren = True
            parens.append(c)
        elif c == ')':
            in_paren = False
            parens.append(c)
        if in_paren:
            parens.append(c)
    return paren
