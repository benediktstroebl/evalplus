from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups = []
    open_paren_stack = []

    for i, c in enumerate(paren_string):
        if c == '(':
            open_paren_stack.append(i)
        elif c == ')':
            groups.append(paren_string[open_paren_stack.pop():i + 1])

    return groups

