from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result: List[str] = []
    s = paren_string.replace(' ', '')
    if len(s) == 0:
        return result
    if len(s) == 1:
        return [s]
    if s.count('(')!= s.count(')'):
        return [s]
    if s.count('(') == s.count(')'):
        result.append(s)
    return result
    
