from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output = []
    for char in paren_string:
        if char == '(':
            output.append(paren_string[0:])
        elif char == ')':
            output[-1] += ')'
        elif char == '(':
            output[-1] += '('
        if len(output) > 0 and output[-1] == ')':
            output.pop()
    return output

