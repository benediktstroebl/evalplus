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
    i = 0
    while i < len(paren_string):
        current_brace = paren_string[i]
        if current_brace == "(":
            parens.append(paren_string[i:i+1])
        i += 1
        while i < len(paren_string) and paren_string[i] == ")":
            i += 1
    return p
