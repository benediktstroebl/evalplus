from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result: List[str] = []

    paren_group: str = ''

    for char in paren_string:
        if char == '(':
            paren_group += char
        elif char == ')':
            if paren_group:
                result.append(paren_group)
                paren_group = ''
    if paren_group:
        result.append(paren_group)

    return result
