from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separated_parens = []

    open_parens = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            open_parens.append(i)
        if paren_string[i] == ')':
            start = open_parens.pop()
            end = i
            separated_parens.append(paren_string[start + 1:end])
    return separated_parens
