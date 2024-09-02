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
    curr_group = []
    in_group = False

    for ch in paren_string:
        if ch == '(':
            in_group = True
            curr_group.append(ch)
        elif ch == ')':
            curr_group.append(ch)
            in_group = False
            groups.append(''.join(curr_group))
            curr_group = []

    return groups

