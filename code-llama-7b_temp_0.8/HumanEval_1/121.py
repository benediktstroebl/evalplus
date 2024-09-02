from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Base cases:
    if not paren_string:
        return []
    elif len(paren_string) == 1:
        return [paren_string]

    # Recursive cases:
    idx = 1
    while idx < len(paren_string) and paren_string[idx] != ')':
        idx += 1
    return [paren_string[:idx + 1]] + separate_paren_groups(paren_string[idx + 1:])

