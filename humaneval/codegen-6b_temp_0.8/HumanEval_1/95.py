from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    pars = []
    current_group = []
    for c in paren_string:
        if c == '(':
            current_group.append(c)
        elif c == ')':
            current_group.pop()
            if not current_group:
                pars.append(''.join(current_group))
                current_group = []
            else:
                pars.append(''.join(current_group))
                current_group = []
    if current_group:
        pars.append(''.join(current_group))
    return pars

