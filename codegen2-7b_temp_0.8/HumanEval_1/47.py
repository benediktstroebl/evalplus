from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    group = []
    is_open = False
    for c in paren_string:
        if is_open and c == '(':
            groups.append(''.join(group))
            group = []
            is_open = False
        elif c == '(':
            group.append(c)
            is_open = True
        else:
            group.append(c)
    groups.append(''.join(group))
    return groups

