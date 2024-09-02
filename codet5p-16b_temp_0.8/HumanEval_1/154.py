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
    result_groups = []
    for char in paren_string:
        if char == '(':
            if current_group:
                result_groups.append(''.join(current_group))
                current_group = []
            current_group.append(char)
        elif char == ')':
            if current_group:
                current_group.append(char)
            else:
                current_group.append(char)
        else:
            if current_group:
                current_group.append(char)
            else:
                result_groups.append(char)

    if current_group:
        result_groups.append(''.join(current_group))

    return result_groups

