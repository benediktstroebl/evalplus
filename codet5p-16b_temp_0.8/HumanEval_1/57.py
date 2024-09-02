from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_groups = []
    group = ''
    for char in paren_string:
        if char == '(':
            group += char
        elif char == ')' and group:
            group += char
            paren_groups.append(group)
            group = ''
        elif char == ')' and not group:
            group += char
            paren_groups.append(group)
            group = ''
    return paren_groups
