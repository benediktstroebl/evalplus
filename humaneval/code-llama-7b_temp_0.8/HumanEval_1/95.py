from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # split the input string into groups of parentheses
    paren_group = [s for s in paren_string.split(")") if s != ""]
    # call _separate_paren_group for each group of parentheses
    return [_separate_paren_group(paren_group) for paren_group in paren_group]

