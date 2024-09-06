from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) < 1:
        return []

    if len(paren_string) == 1:
        if paren_string == '(':
            return ['()']
        else:
            return []

    current_group = ''
    groups = []
    depth = 0
    for paren in paren_string:
        if paren == '(':
            depth += 1
        if paren == ')':
            depth -= 1
        if depth == 0:
            groups.append(current_group + paren)
            current_group = ''
        else:
            current_group += paren
    return groups

