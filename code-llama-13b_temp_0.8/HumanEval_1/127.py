from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    if len(paren_string) == 1:
        return [paren_string]
    # remove_spaces = paren_string.replace(" ", "")
    # add_spaces_back = remove_spaces[0::3] + " " + remove_spaces[1::3] + " " + remove_spaces[2::3]
    # return add_spaces_back
    return paren_string.replace("(", " ( ").replace(")", " ) ").split()

