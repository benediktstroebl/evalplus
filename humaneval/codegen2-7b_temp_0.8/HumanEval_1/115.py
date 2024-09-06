from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    res = []
    start = 0
    end = 0
    while end < len(paren_string):
        if paren_string[end] == '(':
            start = end
        elif paren_string[end] == ')':
            res.append(paren_string[start:end + 1])
            end += 1
        end += 1
    return
