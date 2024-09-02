from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nest_count = 1
    nesting = 0
    current = []
    for char in paren_string:
        if char == '(':
            nesting += 1
        elif char == ')':
            nesting -= 1
        elif nesting == 0:
            current.append(char)
        elif nesting > 0 and nesting < nest_count:
            nest_count = nesting
            current.append(char)
    return current

