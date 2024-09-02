from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_groups = []
    group = ''
    open_braces = 0
    for i, c in enumerate(paren_string):
        if c == '(':
            open_braces += 1
        if c == ')':
            open_braces -= 1
            if open_braces == 0:
                group += paren_string[:i + 1]
                paren_groups.append(group)
                group = ''
                open_braces = 0
    return paren_groups
