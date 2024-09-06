from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parentheses = []
    stack = []

    for i, ch in enumerate(paren_string):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                parentheses.append(paren_string[stack[-1]:i + 1])
            stack.pop()
    if stack:
        parentheses.append(paren_string[stack[-1]:])

    return parentheses

