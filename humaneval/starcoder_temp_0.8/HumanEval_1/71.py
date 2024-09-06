from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    current_group = []
    group_is_open = False
    for char in paren_string:
        if char == "(":
            if group_is_open:
                current_group.append(char)
            else:
                group_is_open = True
        elif char == ")":
            if group_is_open:
                current_group.append(char)
            else:
                continue
        if char == " " and group_is_open:
            result.append("".join(current_group))
            current_group = []
            group_is_open = False
    if group_is_open:
        result.append("".join(current_group))
    return result
