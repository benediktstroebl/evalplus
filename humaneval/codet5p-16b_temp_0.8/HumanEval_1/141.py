from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    assert paren_string.count('(') == paren_string.count(')')
    groups: List[str] = []
    current_group = ''
    for c in paren_string:
        if c == '(':
            if current_group!= '':
                groups.append(current_group)
            current_group = ''
        elif c == ')':
            if current_group!= '':
                groups.append(current_group)
            current_group = ''
        else:
            current_group += c
    return groups
    pass
