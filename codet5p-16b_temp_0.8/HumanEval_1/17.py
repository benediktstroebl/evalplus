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
    temp = []
    for idx in range(len(paren_string)):
        if paren_string[idx] == '(':
            temp.append(paren_string[idx])
        elif paren_string[idx] == ')':
            temp.append(paren_string[idx])
            separated_groups.append(''.join(temp))
            temp = []

    return separated_groups

