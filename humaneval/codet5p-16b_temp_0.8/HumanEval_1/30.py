from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    group = ''
    count = 0
    for c in paren_string:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count == 0:
            group += c
            result.append(group)
            group = ''
        elif count > 0:
            group += c
    return result
