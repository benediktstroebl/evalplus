from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    opening_parens = []
    for char in paren_string:
        if char == '(':
            opening_parens.append(char)
        elif char == ')':
            if len(opening_parens) == 0:
                raise Exception('Unbalanced parentheses')
            opening_parens.pop()
    if len(opening_parens) > 0:
        raise Exception('Unbalanced parentheses')
    return paren_string.split(' ')

