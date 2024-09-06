from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    current_group = []
    final_list = []
    for paren in paren_string:
        if paren == '(':
            current_group.append(paren)
        elif paren == ')':
            if len(current_group) == 0:
                raise ValueError('Mismatched parentheses')
            current_group.append(paren)
            if len(current_group) == 1:
                final_list.append(''.join(current_group))
            else:
                final_list.append(''.join(current_group[1:-1]))
                current_group = []
    if len(current_group) != 0:
        final_list.append(''.join(current_group))
    return final_list

