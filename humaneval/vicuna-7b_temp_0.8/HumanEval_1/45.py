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
        open_brace = paren_string[i]
        i = i + 1
        while open_brace == '(':
            if i == len(paren_string) or paren_string[i] != '(':
                break
            i += 1
        result.append(paren_string[i:])
    return result

