from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    paren_group = ''
    results = []
    for c in paren_string:
        if c == '(':
            paren_group += c
        elif c == ')':
            results += separate_paren_groups(paren_group)
            paren_group = ''
        else:
            paren_group += c
    if paren_group != '':
        results += separate_paren_groups(paren_group)
    return results

