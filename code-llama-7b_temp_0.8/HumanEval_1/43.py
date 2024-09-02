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
    curr_group: List[str] = []
    in_group = False
    for c in paren_string:
        if in_group:
            curr_group.append(c)
            if c == ')':
                in_group = False
                groups.append(''.join(curr_group))
                curr_group = []
        else:
            if c == '(':
                in_group = True
                curr_group.append(c)
    return groups

