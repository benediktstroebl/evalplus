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
    open_paren = '('
    close_paren = ')'
    start = 0
    end = 0

    for i, c in enumerate(paren_string):
        if c == open_paren:
            start = i

        if c == close_paren:
            end = i
            group = paren_string[start:end + 1]
            groups.append(group)
            start = end + 1

    return groups

