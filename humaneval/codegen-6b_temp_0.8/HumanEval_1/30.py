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
    start_index = 0
    while start_index < len(paren_string):
        match_index = paren_string.find('()', start_index)
        if match_index == -1:
            paren_groups.append(paren_string[start_index:])
            break
        paren_groups.append(paren_string[start_index:match_index])
        start_index = match_index + 2
    return paren_groups

