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
    paren_stack = []
    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
        elif char == ')':
            if not paren_stack:
                groups.append('')
            else:
                groups[-1] += ''.join(paren_stack)
                paren_stack.pop()

    if paren_stack:
        groups.append(''.join(paren_stack))

    return groups
