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
    group = ''
    in_group = False
    for char in paren_string:
        if char == '(' and not in_group:
            in_group = True
            group = ''
        elif char == ')' and in_group:
            in_group = False
            groups.append(group)
            group = ''
        else:
            group += char
    groups.append(group)
    return groups

