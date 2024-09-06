from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nested_parens = []
    current_open_parens = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            if current_open_parens > 0:
                nested_parens.append(paren_string[i-1:i])
            current_open_parens += 1
        elif c == ')':
            current_open_parens -= 1
            if current_open_parens == 0:
                nested_parens.append(paren_string[i:i+1])
    return nested_parens