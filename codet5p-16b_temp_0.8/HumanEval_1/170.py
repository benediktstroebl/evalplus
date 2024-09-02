from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string == '':
        return []

    groups = []
    current_group = []
    in_parens = False
    for char in paren_string:
        if char == '(':
            in_parens = True
            current_group.append(char)
        elif char == ')':
            in_parens = False
            current_group.append(char)
            groups.append(''.join(current_group))
            current_group = []
        else:
            current_group.append(char)

    if len(current_group) > 0:
        groups.append(''.join(current_group))
    return groups

