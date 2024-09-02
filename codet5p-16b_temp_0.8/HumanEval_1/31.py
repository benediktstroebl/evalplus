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
    current_group = []
    is_opening_bracket = True
    for c in paren_string:
        if c == '(' and is_opening_bracket:
            current_group.append(c)
        elif c == '(' and not is_opening_bracket:
            paren_groups.append(''.join(current_group))
            current_group = []
            current_group.append(c)
        elif c == ')' and not is_opening_bracket:
            current_group.append(c)
        elif c == ')' and is_opening_bracket:
            current_group.append(c)
            is_opening_bracket = False
        else:
            current_group.append(c)

    paren_groups.append(''.join(current_group))

    return paren_groups

