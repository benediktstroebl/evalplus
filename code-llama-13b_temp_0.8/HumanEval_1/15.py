from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start = balanced = 0
    res = []
    for index, char in enumerate(paren_string):
        if char == '(':
            balanced += 1
        elif char == ')':
            balanced -= 1
        if balanced == 0:
            res.append(paren_string[start : index + 1])
            start = index + 1
    return res

