from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    ret = []
    paren_stack = []

    for char in paren_string:
        if char == '(':
            paren_stack.append(char)
        elif char == ')':
            if not paren_stack:
                raise Exception("Unmatched parenthesis: '%s'" % char)
            paren_stack.pop()

        if paren_stack:
            ret.append(paren_stack.pop())

    while paren_stack:
        ret.append(paren_stack.pop())
    return
