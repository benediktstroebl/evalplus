from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_group = []
    group = []
    paren_string = paren_string.replace(' ','')
    for ch in paren_string:
        if ch == '(':
            paren_group.append('(')
            group.append(ch)
        if ch == ')':
            paren_group.pop()
            group.append(ch)
        if not paren_group:
            group.append(ch)
            break
    return group
            
