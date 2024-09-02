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
    open_list = []
    for c in paren_string:
        if c == '(':
            open_list.append('(')
        elif c == ')':
            if len(open_list) == 0:
                res.append('')
            else:
                open_list.pop()

    if len(open_list) == 0:
        res.append('')

    return res

