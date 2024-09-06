from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    curr_paren_str = ''
    paren_groups = []

    for char in paren_string:
        if char == '(':
            curr_paren_str += '('
        elif char == ')':
            curr_paren_str += ')'
            paren_groups.append(curr_paren_str)
            curr_paren_str = ''

    return paren_groups

