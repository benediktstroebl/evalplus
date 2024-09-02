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
    depth = 0
    start = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            depth += 1
            if depth == 1:
                paren_groups.append(paren_string[start:i])
                start = i + 1

        if c == ')':
            depth -= 1
            if depth == 0:
                paren_groups.append(paren_string[start: i + 1])
                start = i + 1

    return paren_groups

