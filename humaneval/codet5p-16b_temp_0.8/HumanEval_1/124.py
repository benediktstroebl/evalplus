from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None:
        raise TypeError('Empty String')

    stack = []
    output = []
    for char in paren_string:
        if char == ')':
            stack.pop()
        else:
            stack.append(char)
        if len(stack) == 0:
            output.append(paren_string[0:len(paren_string) - len(stack) + 1])

    return output

