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
    current_paren_group = ''
    for i in range(len(paren_string)):
        if paren_string[i] == ')':
            if len(current_paren_group) > 0:
                current_paren_group += ')'
            paren_groups.append(current_paren_group)
            current_paren_group = ''
        elif paren_string[i] == '(':
            if len(current_paren_group) > 0:
                current_paren_group += '('
            else:
                current_paren_group += '('
        else:
            current_paren_group += paren_string[i]
    if len(current_paren_group) > 0:
        paren_groups.append(current_paren_group)
    return paren_groups

