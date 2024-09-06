from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    open_count, paren_count = 0, 0
    for i, paren in enumerate(paren_string):
        if paren == '(':
            open_count += 1
        elif paren == ')':
            open_count -= 1
        if open_count == 0:
            groups.append(paren_string[paren_count + 1: i + 1])
            paren_count = i + 1
    return groups

