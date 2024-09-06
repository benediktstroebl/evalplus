from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_idx = 0
    result = []
    for idx, val in enumerate(paren_string):
        if val == '(':
            start_idx = idx
        elif val == ')' and start_idx != 0:
            result.append(paren_string[start_idx:idx + 1])
            start_idx = 0
    return result

