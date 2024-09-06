from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    current_string = paren_string.replace(' ', '')
    open_parens = []
    close_parens = []
    result = []

    for p in current_string:
        if p == '(':
            open_parens.append(p)
        elif p == ')':
            if open_parens:
                open_parens.pop()
            else:
                close_parens.append(p)

    if open_parens:
        result.append(current_string)
    else:
        current_string = current_string.replace('(', '')
        current_string = current_string.replace(')', '')
        result = current_string.split()

    if close_parens:
        result.append(current_string)
    else:
        current_string = current_string.replace(')', '')
        result = current_string.split()

    return result

