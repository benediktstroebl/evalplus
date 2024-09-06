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
    bracket_groups = []
    for paren in paren_string:
        if paren == '(':
            open_parens.append(paren)
        elif paren == ')':
            if len(open_parens) > 0:
                open_parens.pop()
            else:
                bracket_groups.append(''.join(open_parens))
                open_parens = []
        else:
            bracket_groups.append(paren)

    return bracket_groups
