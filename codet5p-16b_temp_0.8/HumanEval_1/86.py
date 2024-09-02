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
    bracket_groups = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(' or paren_string[i] == ')':
            open_bracket = paren_string[i]
            close_bracket = paren_string[i+1]
            if open_bracket == ')' and close_bracket == '(':
                bracket_groups.append(paren_string[i: i+2])
                i += 1
            else:
                bracket_groups.append(open_bracket)
        i += 1
    return bracket_groups

