from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    current_group = ""
    start = 0
    end = 0
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            start = i
        elif paren_string[i] == ")":
            end = i
            current_group = paren_string[start:end + 1]
            groups.append(current_group)
            start = end + 1

    return groups

