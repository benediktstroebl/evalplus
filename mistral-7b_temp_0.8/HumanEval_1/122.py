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
    i = 0
    while i < len(paren_string):
        group_start_index = i
        if paren_string[i] == '(':
            i += 1
        elif paren_string[i] == ')':
            group_end_index = i
            i += 1
        else:
            i += 1
        groups.append(paren_string[group_start_index:group_end_index + 1])

    return groups

