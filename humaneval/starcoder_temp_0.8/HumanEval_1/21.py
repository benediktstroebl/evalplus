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

    balancing = 0

    current_group = ""

    for char in paren_string:
        if char == "(":
            balancing += 1
        elif char == ")":
            balancing -= 1

        if balancing == 0:
            paren_groups.append(current_group)
            current_group = ""
        else:
            current_group += char

    return paren_groups

