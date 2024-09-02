from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    group_list = []
    start = 0
    end = 0
    in_group = False
    for index, char in enumerate(paren_string):
        if char == '(':
            if not in_group:
                start = index
            in_group = True
        elif char == ')':
            if in_group:
                end = index
                group_list.append(paren_string[start:end + 1])
                in_group = False
    return group_list

