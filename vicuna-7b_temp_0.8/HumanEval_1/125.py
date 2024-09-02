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
    output = []
    open_parens = 0
    for char in paren_string:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
        elif open_parens == 0:
            output.append(paren_string[stack[-1]:])
            stack.pop()
        else:
            stack.append(char)
    output.append(paren_string[stack[-1]:])
    return output

