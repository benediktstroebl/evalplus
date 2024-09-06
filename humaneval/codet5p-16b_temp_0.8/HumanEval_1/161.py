from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = [paren_string]
    separated_paren_list = []
    while paren_list:
        paren_string = paren_list.pop()
        paren_groups = separate_paren_groups_helper(paren_string)
        for paren_group in paren_groups:
            paren_list.append(paren_group)
    for paren_group in paren_list:
        if is_balanced(paren_group):
            separated_paren_list.append(paren_group)
    return separated_paren_list

