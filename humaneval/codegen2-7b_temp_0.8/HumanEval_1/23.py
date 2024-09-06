from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    group_stack = []
    for c in paren_string:
        if c == '(':
            group_stack.append(c)
        elif c == ')':
            if len(group_stack) > 0:
                group_stack.pop()
            else:
                group_stack.append(c)
        elif len(group_stack) == 0:
            group_stack.append(c)
    return group_
