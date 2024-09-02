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
    opener_count = 0
    closer_count = 0
    for c in paren_string:
        if c == '(':
            opener_count += 1
        elif c == ')':
            closer_count += 1
        else:
            continue
        if opener_count == closer_count:
            res.append(paren_string[opener_count-closer_count:])
    return res
