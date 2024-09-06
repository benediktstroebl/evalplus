from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    list_of_paren_groups = []
    temp = []
    for paren in paren_string:
        if paren == "(":
            temp.append(paren)
        elif paren == ")":
            temp.append(paren)
            list_of_paren_groups.append("".join(temp))
            temp = []

    return list_of_paren_groups

