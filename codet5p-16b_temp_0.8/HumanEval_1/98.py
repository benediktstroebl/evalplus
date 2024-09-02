from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    pass
    paren_stack: List[str] = []
    paren_group: List[str] = []

    for c in paren_string:
        if c == '(':
            paren_stack.append(c)
        elif c == ')':
            if len(paren_stack) > 0 and paren_stack[-1] == '(':
                paren_stack.pop()
                paren_group.append('(')
            else:
                paren_stack.append(')')

    return [''.join(group) for group in separate_paren_groups]

