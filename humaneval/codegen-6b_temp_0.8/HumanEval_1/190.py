from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    ret, stack = [], []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                raise Exception("Unexpected ')'")
            stack.pop(-1)
        elif c == ' ':
            continue

        if not stack:
            ret.append(c)
    return ret

