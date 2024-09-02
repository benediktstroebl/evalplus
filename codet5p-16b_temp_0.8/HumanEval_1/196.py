from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []
    stack = []
    for i in paren_string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            elif len(stack) == 0:
                stack.append(i)
        else:
            pass

    while len(stack) > 0:
        result.append(''.join(stack))
        stack = []
    return result

