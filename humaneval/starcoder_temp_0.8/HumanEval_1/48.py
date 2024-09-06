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

    i = 0
    groups = []

    while i < len(paren_string):
        # Check for empty group
        if paren_string[i] == '(':
            next_close_paren_index = paren_string.find(')', i)
            if next_close_paren_index!= -1:
                groups.append(paren_string[i + 1:next_close_paren_index])
                i = next_close_paren_index
            else:
                return []
        else:
            return []
    return groups

