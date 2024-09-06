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
    paren_stack: List[str] = []

    for c in paren_string:
        if c == '(':
            paren_stack.append(c)
        elif c == ')':
            if len(paren_stack) == 0:
                continue
            else:
                paren_stack.pop()
        else:
            result.append(''.join(paren_stack))
            paren_stack = []

    if len(paren_stack) > 0:
        result.append(''.join(paren_stack))

    return result

