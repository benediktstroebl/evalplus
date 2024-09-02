from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    assert all(char in '()[]{}' for char in paren_string)

    paren_groups = []
    count = 0
    current = ''
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        elif count == 0:
            paren_groups.append(current)
            current = ''
        current += char
    paren_groups.append(current)

    return paren_groups

