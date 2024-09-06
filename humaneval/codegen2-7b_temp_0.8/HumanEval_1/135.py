from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []

    result = []

    opened = 0
    stack = []

    for char in paren_string:
        if char == '(':
            opened += 1
            stack.append(char)
        elif char == ')':
            if opened > 0:
                stack.pop()
                opened -= 1
            else:
                result.append(''.join(stack))
                stack = []
        else:
            stack.append(char)

    return result
