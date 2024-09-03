from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    for paren in paren_string.split():
        paren_group = []
        paren_index = paren.find('(')
        if paren_index == -1:
            paren_group.append(paren)
            paren_groups.append(paren_group)
        else:
            paren_group.append(paren[paren_index + 1:])
    return paren_groups

