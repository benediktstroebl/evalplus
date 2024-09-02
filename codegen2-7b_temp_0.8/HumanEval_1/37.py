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
    for i, group in enumerate(paren_string):
        if group == '(':
            open_groups = 1
            open_parens = ''
        elif group == ')':
            if open_groups == 1:
                result.append(f'({open_parens})')
                open_groups = 0
            elif open_groups == 0:
                result.append(f'{open_parens}')
        else:
            open_parens += group
            open_groups += 1
    return
