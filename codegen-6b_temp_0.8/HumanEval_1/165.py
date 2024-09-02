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
    stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            stack.append(i)
        else:
            if stack:
                j = stack.pop()
                res.append(paren_string[j + 1: i])
            else:
                res.append('')
        i += 1
    if stack:
        m = stack.pop()
        res.append(paren_string[m + 1:])
    return res

