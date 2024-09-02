from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []
    parens = []
    open_parens = 0
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            open_parens += 1
        elif paren_string[i] == ')':
            open_parens -= 1
        if open_parens == 0:
            parens.append(paren_string[i + 1:])
        i += 1
    return paren
