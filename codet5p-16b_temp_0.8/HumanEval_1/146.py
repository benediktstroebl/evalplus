from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    brackets_open = '({['
    brackets_close = ')}]'
    paren_groups = []
    while paren_string:
        next_open_paren = paren_string.find(brackets_open)
        next_close_paren = paren_string.find(brackets_close, next_open_paren + 1)
        paren_groups.append(paren_string[:next_open_paren])
        paren_string = paren_string[next_open_paren + 1:next_close_paren + 1]
    return paren_groups

