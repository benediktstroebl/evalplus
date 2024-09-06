from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string is None or len(paren_string) == 0:
        return []
    stack = []
    paren_groups = []
    for s in paren_string:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if stack:
                stack.pop()
            else:
                paren_groups.append('')
                continue
    while stack:
        paren_groups.append(stack.pop())

    return paren_groups

