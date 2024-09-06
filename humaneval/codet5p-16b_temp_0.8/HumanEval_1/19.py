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
    open_parens = []
    for c in paren_string:
        if c == '(':
            open_parens.append(c)
        elif c == ')':
            if len(open_parens) == 0:
                raise ValueError("Too many closed parentheses.")
            open_parens.pop()
        else:
            continue
    if len(open_parens) > 0:
        raise ValueError("Too many open parentheses.")

    while len(paren_groups) < len(open_parens):
        paren_groups.append("".join(open_parens))
        open_parens = open_parens[1:]

    return paren_groups

