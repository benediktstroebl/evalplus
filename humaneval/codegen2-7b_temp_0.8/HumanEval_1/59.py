from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_strings: List[str] = []
    start_paren = paren_string.index('(')
    end_paren = paren_string.rindex(')')

    while start_paren!= -1 and end_paren!= -1:
        if start_paren == end_paren - 1:
            paren_strings.append(paren_string[start_paren + 1:end_paren])
        start_paren = paren_string.index('(', end_paren + 1)
        end_paren = paren_string.rindex(')', start_paren)

    return paren_
