from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    left, right = 0, 0
    groups = []
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append(i)
        elif c == ')':
            if len(stack) == 0:
                raise IndexError(i)
            stack.pop()
            groups.append(paren_string[left + 1: i])
            left = i + 1
    return groups

