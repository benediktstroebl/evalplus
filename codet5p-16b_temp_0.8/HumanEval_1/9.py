from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = []
    substring_list = []
    is_open_paren = False
    for char in paren_string:
        if char == '(':
            is_open_paren = True
            substring_list = []
            continue
        if char == ')':
            if is_open_paren:
                is_open_paren = False
                paren_list.append(substring_list)
                continue
        if is_open_paren:
            substring_list.append(char)
    return paren_list

