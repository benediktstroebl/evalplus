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
    split_paren_string = paren_string.split()
    for paren_group in split_paren_string:
        curr_paren_group = ""
        for paren in paren_group:
            if paren == "(":
                curr_paren_group += paren
            elif paren == ")":
                curr_paren_group = curr_paren_group[:-1]
            if curr_paren_group == "":
                paren_groups.append(paren_group)
                break
    return paren_groups

