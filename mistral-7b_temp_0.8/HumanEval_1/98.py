from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    open_parens = 0
    closed_parens = 0
    parens = ""
    for letter in paren_string:
        if letter == '(':
            open_parens += 1
            closed_parens -= 1
        elif letter == ')':
            open_parens -= 1
            closed_parens += 1
        if closed_parens == 0:
            paren_groups.append(parens)
            open_parens = 0
            closed_parens = 0
            parens = ""
        parens += letter
    paren_groups.append(parens)
    return paren_groups
