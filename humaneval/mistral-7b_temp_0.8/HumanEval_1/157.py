from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list: List[str] = []
    cur_paren_group: str = ''
    for paren in paren_string:
        if paren == '(':
            cur_paren_group += paren
        elif paren == ')':
            if cur_paren_group:
                cur_paren_group += paren
            else:
                paren_list.append(cur_paren_group)
                cur_paren_group = ''
    if cur_paren_group:
        paren_list.append(cur_paren_group)
    return paren_list

