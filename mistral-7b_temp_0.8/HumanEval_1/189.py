from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    res = []
    in_paren = 0
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            in_paren += 1
        if paren_string[i] == ')':
            in_paren -= 1
        if in_paren == 0:
            res.append(paren_string[i])
        i += 1
    return res

