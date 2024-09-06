from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []

    if paren_string[0] != '(':
        raise ValueError('Invalid parentheses: expected "("')

    if paren_string[-1] != ')':
        raise ValueError('Invalid parentheses: expected ")"')

    open_parens = 0
    paren_groups = []
    current_group = ''
    for character in paren_string:
        current_group += character
        if character == '(':
            open_parens += 1
        elif character == ')':
            open_parens -= 1
        if open_parens == 0:
            paren_groups.append(current_group)
            current_group = ''

    return paren_groups

