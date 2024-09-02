from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []

    paren_stack = []
    open_braces = 0
    braces_to_open = 0
    braces_to_close = 0
    groups = []
    open_braces_string = ''
    for char in paren_string:
        if char == '(' and open_braces == 0:
            open_braces += 1
            open_braces_string += '('
        elif char == ')' and open_braces == 1:
            open_braces -= 1
            open_braces_string += ')'
        elif char == '(' and open_braces == 0:
            braces_to_open += 1
            braces_to_close = 0
        elif char == ')' and open_braces == 1:
            braces_to_close += 1
            braces_to_open = 0
        elif char == '(':
            braces_to_close += 1
        elif char == ')':
            if braces_to_close == braces_to_open:
                groups.append(open_braces_string)
                open_braces_string = ''
                braces_to_open = 0
                braces_to_close = 0
            elif braces_to_close > braces_to_open:
                open_braces_string += ')'
                braces_to_close -= 1
            elif braces_to_close < braces_to_open:
                open_braces_string += '('
                braces_to_open += 1

    groups.append(open_braces_string)
    return groups

