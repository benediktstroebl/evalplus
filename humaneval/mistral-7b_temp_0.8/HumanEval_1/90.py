from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    separated_strings = []
    open_parens = 0
    closed_parens = 0
    current_group = ''
    for c in paren_string:
        if c == '(':
            open_parens += 1
        elif c == ')':
            closed_parens += 1
        if open_parens == closed_parens:
            current_group += c
            separated_strings.append(current_group)
            current_group = ''
            open_parens = 0
            closed_parens = 0
    return separated_strings
