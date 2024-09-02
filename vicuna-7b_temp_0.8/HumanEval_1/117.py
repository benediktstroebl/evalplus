from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    balanced_groups = []
    current_group = []
    for opening_brace in paren_string:
        if opening_brace == '(':
            current_group.append('(')
        else:
            balanced_groups.append(current_group)
            current_group = []
            if closing_brace == ')' or len(current_group) == 1:
                current_group.append(')')
    balanced_groups.append(current_group)
    return balanced_groups

