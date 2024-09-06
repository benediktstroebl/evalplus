from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parenthesis_groups = []
    open_parens = 0
    close_parens = 0
    for char in paren_string:
        if char == '(':
            open_parens += 1
        if char == ')':
            close_parens += 1
        if open_parens == close_parens:
            parenthesis_groups.append(paren_string[:open_parens+close_parens])
            paren_string = paren_string[open_parens+close_parens:]
            open_parens = 0
            close_parens = 0
    if open_parens > 0 or close_parens > 0:
        raise Exception("Invalid Input")
    return parenthesis_groups

