from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Separate the string into individual groups
    paren_groups = paren_string.split(' ')
    paren_list = []

    # Iterate over each group and check if it contains parentheses
    for paren_group in paren_groups:
        if paren_group != '':
            paren_list.append(paren_group)

    return paren_list

