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
    group_char_list = []
    for char in paren_string:
        if char == "(":
            group_char_list.append(char)
        elif char == ")":
            group_char_list.append(char)
            groups.append(''.join(group_char_list))
            group_char_list = []
    return groups

