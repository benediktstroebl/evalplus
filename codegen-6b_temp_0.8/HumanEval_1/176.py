from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens = []
    start = 0
    for i, paren in enumerate(paren_string):
        if paren == '(':
            if i != 0:
                parens.append(paren_string[start:i])
                start = i
        elif paren == ')':
            if i != len(paren_string) - 1:
                parens.append(paren_string[start:i + 1])
                start = i + 1
    return parens

