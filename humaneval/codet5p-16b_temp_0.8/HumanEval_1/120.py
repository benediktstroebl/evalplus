from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    pass
    result = []
    open_paren_count = 0
    for paren in paren_string:
        if paren == '(':
            open_paren_count += 1
        elif paren == ')':
            open_paren_count -= 1
        if open_paren_count == 0:
            result.append(paren_string[0: paren_string.index(paren) + 1])
            paren_string = paren_string[paren_string.index(paren) + 1:]
            open_paren_count = 0
    return result

