from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    left, right = 0, 0
    res = []
    is_balanced = False
    for s in paren_string:
        if s == '(' and is_balanced:
            is_balanced = False
            res.append(paren_string[left:right])
        if s == '(':
            left = right
            is_balanced = True
        right += 1
    res.append(paren_string[left:right])
    return res

