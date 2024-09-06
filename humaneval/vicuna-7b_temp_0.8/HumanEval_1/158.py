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
    i = 0
    while i < len(paren_string):
        open_brace = paren_string.find('{', i)
        close_brace = paren_string.find('}', open_brace)
        if (open_brace >= 0 and close_brace >= 0):
            result.append(paren_string[i:open_brace + 1])
            i = close_brace + 1
        else:
            result.append(paren_string[i])
            i += 1
    return result

