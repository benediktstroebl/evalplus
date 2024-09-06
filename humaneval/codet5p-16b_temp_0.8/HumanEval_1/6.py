from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result = []

    curr_group = ''
    paren_depth = 0

    for c in paren_string:
        if c == '(':
            paren_depth += 1
            curr_group += c
        elif c == ')':
            paren_depth -= 1
            curr_group += c
            if paren_depth == 0:
                result.append(curr_group)
                curr_group = ''
        else:
            curr_group += c

    return result
