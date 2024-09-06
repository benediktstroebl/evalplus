from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # first, get rid of the spaces
    no_space_string = paren_string.replace(" ", "")
    # separate the groups
    groups = no_space_string.split(")")
    # clean up the results
    new_groups = []
    for group in groups:
        new_groups.append(group + ")")
    return new_groups

