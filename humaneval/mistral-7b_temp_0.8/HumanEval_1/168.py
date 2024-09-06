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
    current_group = ""

    for c in paren_string:
        if c in '([{':
            current_group += c
        elif c in ')]}':
            if current_group and current_group[-1] == c[0]:
                current_group = current_group[:-1]
            else:
                paren_groups.append(current_group)
                current_group = c
        else:
            current_group += c

    paren_groups.append(current_group)

    return paren_groups

