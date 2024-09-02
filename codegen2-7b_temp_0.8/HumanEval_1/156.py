from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    separate_paren_groups_string = ''
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            separate_paren_groups_string +='' + paren_string[i]
        elif paren_string[i] == ')':
            separate_paren_groups_string += paren_string[i]
            return separate_paren_groups_string.split()
    return separate_paren_groups_string.split
