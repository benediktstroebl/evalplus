from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None or len(paren_string) == 0:
        return []

    stack = []

    for ch in paren_string:
        if ch == '(' or ch == ')':
            stack.append(ch)

    output = []

    while len(stack) > 0:
        if len(output) == 0:
            output.append('')

        curr_char = stack.pop(0)
        if curr_char == '(':
            output[-1] += '('
        else:
            output[-1] += ')'

    return output

