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
    in_group = False
    group = ''
    for char in paren_string:
        if in_group and char == ')':
            in_group = False
            groups.append(group[1:-1])
            group = ''
        else:
            if char == '(':
                in_group = True
                group += char
            else:
                group += char
    if in_group:
        groups.append(group[1:-1])
    return
