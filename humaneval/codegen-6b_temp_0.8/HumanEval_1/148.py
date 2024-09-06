from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    results = []
    i = 0
    while i < len(paren_string):
        open_paren = 1
        close_paren = 1
        parens = []
        while open_paren > close_paren and i < len(paren_string):
            if paren_string[i] == "(":
                open_paren += 1
            elif paren_string[i] == ")":
                close_paren += 1
            i += 1
        results.append(paren_string[(i - open_paren):(i - close_paren)])
    return results

