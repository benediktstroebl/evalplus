from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []

    if paren_string[0] != '(':
        return []

    if paren_string[1] == ')':
        return [paren_string[0:2]] + separate_paren_groups(paren_string[2:])

    current_str, i = paren_string[0], 1
    while i < len(paren_string):
        if paren_string[i] == '(':
            current_str += paren_string[i]
        elif paren_string[i] == ')':
            current_str += paren_string[i]
            return [current_str] + separate_paren_groups(paren_string[i + 1:])
        else:
            current_str += paren_string[i]
        i += 1
    return []

