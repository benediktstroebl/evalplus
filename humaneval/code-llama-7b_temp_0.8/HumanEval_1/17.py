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
    current_group = ""

    for c in paren_string:
        if c == '(':
            current_group += c
        elif c == ')':
            current_group += c
            groups.append(current_group)
            current_group = ""
        else:
            # just ignore the char
            pass

    # deal with leftover groups
    for group in groups:
        if group[-1] == ')':
            group = group[1:]
        if group[0] == '(':
            group = group[1:]

    return groups

