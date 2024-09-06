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
    paren_stack = []
    for i, c in enumerate(paren_string):
        if c == '(':
            paren_stack.append(i)
        elif c == ')':
            if paren_stack:
                result.append(paren_string[paren_stack.pop():i+1])
    return result

