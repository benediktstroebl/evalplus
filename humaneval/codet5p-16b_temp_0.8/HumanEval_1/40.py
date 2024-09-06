from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string is None:
        return None
    curr_group = []
    curr_level = 0
    groups = []
    for char in paren_string:
        if char == '(' and curr_level == 0:
            if len(curr_group) > 0:
                groups.append(''.join(curr_group))
                curr_group = []
            curr_level += 1
            groups.append(char)
        elif char == ')' and curr_level == 1:
            curr_level -= 1
            groups.append(char)
        else:
            curr_group.append(char)
    if len(curr_group) > 0:
        groups.append(''.join(curr_group))
    return groups
