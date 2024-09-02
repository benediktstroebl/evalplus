from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string[0] == ')':
        raise Exception('Input string must be balanced and not contain nested parentheses.')
    result = []
    stack = []
    while paren_string:
        if paren_string[0] == '(':
            stack.append(paren_string[0])
        elif paren_string[0] == ')':
            stack.pop()
            if not stack:
                result.append(''.join(stack))
                stack = []
        paren_string = paren_string[1:]
    return result

