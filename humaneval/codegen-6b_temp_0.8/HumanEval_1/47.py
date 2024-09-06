from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    if len(paren_string) == 0:
        return []
    elif paren_string[0] == "(":
        paren_list.append("(")
        paren_list.extend(separate_paren_groups(paren_string[1:]))
    elif paren_string[0] == ")":
        paren_list.append(")")
    else:
        paren_list.extend(separate_paren_groups(paren_string[1:]))
    return paren_list

