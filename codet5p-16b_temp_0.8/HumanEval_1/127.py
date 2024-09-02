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
    open_paren_count = 0
    start = 0
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == '(' and open_paren_count == 0:
            start = i
        elif char == '(' and open_paren_count > 0:
            open_paren_count += 1
        elif char == ')':
            open_paren_count -= 1
            if open_paren_count == 0:
                paren_groups.append(paren_string[start:i + 1])
    return paren_groups

