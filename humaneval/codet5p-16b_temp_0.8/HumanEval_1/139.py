from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    curr = []
    groups = []
    for c in paren_string:
        if c == '(':
            curr.append(c)
        elif c == ')':
            if curr:
                curr.pop()
            else:
                groups.append(''.join(curr))
                curr = []

    groups.append(''.join(curr))
    return groups

