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
    open_paren = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            open_paren += 1
            stack.append(paren_string[i])
        elif paren_string[i] == ')':
            if len(stack)!= 0:
                stack.pop()
            elif len(stack) == 0:
                stack.append(paren_string[i])
        else:
            stack.append(paren_string[i])
    paren_groups = []
    for i in range(len(stack)):
        paren_groups.append(''.join(stack[i:]))
    return paren_groups
