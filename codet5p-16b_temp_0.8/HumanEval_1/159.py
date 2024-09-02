from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if not paren_string:
        return []

    groups = []
    stack = []
    i = 0
    while i < len(paren_string):
        paren = paren_string[i]
        if paren == '(':
            stack.append('(')
        elif paren == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                groups.append(''.join(stack))
            else:
                stack.append(')')
        i += 1
    if stack:
        groups.append(''.join(stack))
    return groups
