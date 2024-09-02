from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_parens = []
    while len(paren_string) > 0:
        if paren_string[0] == '(':
            open_parens.append(paren_string[0])
        elif paren_string[0] == ')' and open_parens and open_parens[-1] == '(':
            open_parens.pop()
        paren_string = paren_string[1:]
    return open_paren
