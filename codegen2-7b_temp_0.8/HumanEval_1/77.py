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
    in_group = False
    current_group = ''
    for char in paren_string:
        if char == '(':
            in_group = True
            current_group = ''
        else:
            if in_group:
                current_group += char
            else:
                if len(current_group) > 0:
                    groups.append(current_group)
                current_group = ''
        if not in_group:
            groups.append(current_group)
    return
