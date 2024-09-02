from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_braces = '({['
    close_braces = ')}]'
    stack = []
    for ch in paren_string:
        if ch in open_braces:
            stack.append(ch)
        elif ch in close_braces:
            if len(stack) > 0 and open_braces.index(stack.pop()) == close_braces.index(ch):
                continue
            else:
                stack.append(ch)
    return [''.join(stack)]
