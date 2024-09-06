from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separated_groups = []
    current_group = ''
    open_parens = 0
    for c in paren_string:
        if c == '(':
            if open_parens == 0:
                current_group += c
            open_parens += 1
        if c == ')':
            if open_parens == 1:
                current_group += c
            open_parens -= 1
            if open_parens == 0:
                separated_groups.append(current_group)
                current_group = ''
    if current_group!= '':
        separated_groups.append(current_group)

    return separated_groups
