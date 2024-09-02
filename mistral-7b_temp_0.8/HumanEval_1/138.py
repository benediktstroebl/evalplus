from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_group_list: List[str] = []
    current_paren_group = ""

    for paren in paren_string:
        if paren == "(":
            current_paren_group += paren
        elif paren == ")":
            if current_paren_group != "":
                current_paren_group += paren
                paren_group_list.append(current_paren_group)
                current_paren_group = ""
            else:
                raise ValueError("Unbalanced parentheses")
    if current_paren_group != "":
        paren_group_list.append(current_paren_group)
    return paren_group_list

