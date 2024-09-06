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
    cur_pars_string = ''
    for char in paren_string:
        if char == '(':
            cur_pars_string += '('
        elif char == ')':
            cur_pars_string += ')'
            result.append(cur_pars_string)
            cur_pars_string = ''
    return result
