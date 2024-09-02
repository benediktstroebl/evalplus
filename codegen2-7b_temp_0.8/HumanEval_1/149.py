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
    groups: List[str] = []
    group = ''
    for c in paren_string:
        if c == '(':
            group += c
        elif c == ')':
            if group:
                groups.append(group)
                group = ''
            else:
                group += c
    if group:
        groups.append(group)
    return groups

