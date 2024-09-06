from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups: List[str] = []
    curr_group: str = ''
    depth: int = 0

    for c in paren_string:
        if c == '(':
            if depth > 0:
                curr_group += '('
            depth += 1
        if c == '(':
            if depth > 0:
                curr_group += ')'
            depth -= 1
            if depth == 0:
                groups.append(curr_group)
                curr_group = ''
    return groups

